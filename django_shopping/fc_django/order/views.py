from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from product.models import Product
from .models import Order

from django.utils.decorators import method_decorator
from fcuser.decorators import login_required
# Create your views here.


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    # template_name = 'product_detail.html'
    # 필요가 없음. 화면을 보여주는 용도로 쓰는게 아니기 때문
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        # return redirect('/product/'+str(form.product))
        # return super().form_invalid(form)
        # 이 또한 request를 사용하기 위함.
        product = Product.objects.get(pk=form.product)
        return render(self.request, 'product_detail.html', {'form': form, 'product': product})

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    # model = Order 이러면 모든 쿼리가 다 전달돼
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            fcuser__email=self.request.session.get('user'))
        return queryset
