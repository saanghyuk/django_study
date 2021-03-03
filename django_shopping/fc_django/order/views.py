from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm
# Create your views here.


class OrderCreate(FormView):
    # template_name = 'product_detail.html'
    # 필요가 없음. 화면을 보여주는 용도로 쓰는게 아니기 때문
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/'+str(form.product))
        # return super().form_invalid(form)
        # 이 또한 request를 사용하기 위함.

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
