from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    # 폼에 같이 실어서 보내주는 역할
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # self.request는 form으로 request를 전달해서 세션을 사용하기 위함.
        # 이렇게 넣어 놓으면, 폼을 생성하면서 request를 만듬
        context['form'] = OrderForm(self.request)
        return context
