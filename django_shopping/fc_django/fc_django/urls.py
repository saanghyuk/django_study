"""fc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from order.models import Order
from django.contrib import admin
from django.urls import path, include, re_path
from django.template.response import TemplateResponse
from fcuser.views import index, RegisterView, LoginView, logout
from product.views import ProductList, ProductCreate, ProductDetail, ProductListAPI, ProductDetailAPI
from order.views import OrderCreate, OrderList
from django.views.generic import TemplateView
import datetime
from order.models import Order
from .functions import get_exchange

original_index = admin.site.index


def fastcampus_index(request, extra_context=None):
    base_date = datetime.datetime.now() - datetime.timedelta(days=7)
    order_data = {}
    for i in range(7):
        target_dttm = base_date + datetime.timedelta(days=i)
        date_key = target_dttm.strftime('%Y-%m-%d')
        target_date = datetime.date(
            target_dttm.year, target_dttm.month, target_dttm.day)
        order_cnt = Order.objects.filter(
            register_date__date=target_date).count()
        order_data[date_key] = order_cnt

    order_date = list(order_data.keys())
    order_quantity = list(order_data.values())
    print(type(order_date[1]))
    extra_context = {
        'order_date': order_date,
        'order_quantity': order_quantity,
        'exchange': get_exchange()
    }
    return original_index(request, extra_context)


admin.site.index = fastcampus_index


urlpatterns = [
    path('admin/manual/', TemplateView.as_view(template_name='admin/manual.html',
                                               extra_context={'title': '메뉴얼', 'site_title': '고려화학매트', 'site_header': '고려화학매트'})),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
    path('product/create', ProductCreate.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('order/', OrderList.as_view()),

    path('api/product/', ProductListAPI.as_view()),
    path('api/product/<int:pk>', ProductDetailAPI.as_view())


]
