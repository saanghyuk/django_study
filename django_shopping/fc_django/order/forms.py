from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser


class RegisterForm(forms.Form):

    # 이 생성자는 views의 ProductDetail
    # 내부 get_context_data와 함께 request를 폼에서 사용하기 위함
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요'
        },
        label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요'
        },
        label='상품',
        widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fcuser = self.request.session.get('user', None)

        if quantity and product and fcuser:
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product),
                fcuser=Fcuser.objects.get(email=fcuser)
            )
            order.save()
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')
