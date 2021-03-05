from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm

from django.utils.decorators import method_decorator
from fcuser.decorators import admin_required
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'


@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    # 폼에 같이 실어서 보내주는 역할
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # OrderForm을 Product Detail Page로 넘겨주는 역할
        # self.request는 form으로 request를 전달해서 세션을 사용하기 위함.
        # 이렇게 넣어 놓으면, 폼을 생성하면서 request를 만듬
        # context['form'] = OrderForm()
        context['form'] = OrderForm(self.request)
        return context
