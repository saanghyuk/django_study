
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.template.response import TemplateResponse
from django.urls import path
import datetime

from django.contrib import admin
from .models import Order
from django.utils.html import format_html
from django.db.models import F, Q
# 여러 모델 한번에 바꿀때는 항상 transaction을 사용할 것
from django.db import transaction
# Register your models here.


# 데이터 끼워넣는 다른 방법


def orderComplete(modeladmin, request, queryset):
    with transaction.atomic():
        qs = queryset.filter(~Q(status='결제완료'))

        # ct = ContentType.objects.get_for_model(queryset.model)
        for obj in qs:
            obj.product.stock -= obj.quantity
            obj.product.save()

            # 메인 화면 변경 로그 남기기 위해 정보 주기
            # LogEntry.objects.log_action(
            #     user_id=request.user.id,
            #     content_type_id=ct.pk,
            #     object_id=obj.pk,
            #     object_repr='주문 환불',
            #     action_flag=CHANGE,
            #     change_message="주문 환불",
            # )

        qs.update(status='결제완료')


orderComplete.short_description = '결제완료'


def refund(modeladmin, request, queryset):
    # query셋에는 체크한 애들이 들어옴, 일괄적으로 쓸때만 이렇게 하는 것 같음.
    # queryset.update(obj.product.stock += obj.quantity)
    with transaction.atomic():
        qs = queryset.filter(~Q(status='환불'))

        ct = ContentType.objects.get_for_model(queryset.model)
        for obj in qs:
            obj.product.stock += obj.quantity
            obj.product.save()

            # 메인 화면 변경 로그 남기기 위해 정보 주기
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ct.pk,
                object_id=obj.pk,
                object_repr='주문 환불',
                action_flag=CHANGE,
                change_message="주문 환불",
            )

        qs.update(status='환불')


refund.short_description = '환불'


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'styled_status', 'action')
    change_list_template = 'admin/order_change_list.html'
    change_form_template = 'admin/order_change_form.html'
    # add_form_template = 'admin/order_add_form.html'
    actions = [
        refund,
        orderComplete
    ]

    def action(self, obj):
        if obj.status != '환불':
            return format_html(f'<input type="button" value="환불" onclick="order_refund_submit({obj.id})" class="btn btn-primary btn-sm">')

    def add_view(self, request, extra_context=None):
        # if request.user.is_superuser:
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        # extra_context['show_save'] = False
        # extra_context['show_delete'] = False
        return super(OrderAdmin, self).add_view(request, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        # 우리가 원하는 동작
        extra_context = {'title': '주문 목록'}
        if request.method == 'POST':
            obj_id = request.POST.get('obj_id')
            if obj_id:
                qs = Order.objects.filter(pk=obj_id)

                ct = ContentType.objects.get_for_model(qs.model)
                for obj in qs:
                    obj.product.stock += obj.quantity
                    obj.product.save()

                    # 메인 화면 변경 로그 남기기 위해 정보 주기
                    LogEntry.objects.log_action(
                        user_id=request.user.id,
                        content_type_id=ct.pk,
                        object_id=obj.pk,
                        object_repr='주문 환불',
                        action_flag=CHANGE,
                        change_message="주문 환불",
                    )

                qs.update(status='환불')

        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        try:
            order = Order.objects.get(pk=object_id)
            extra_context = {
                'title': f"'{order.fcuser.email}'님의 '{order.product.name}' 주문"}
            extra_context['show_save_and_add_another'] = False
            extra_context['show_save_and_continue'] = False
        except:
            pass

        return super().changeform_view(request, object_id, form_url, extra_context)

    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        elif obj.status == '결제완료':
            return format_html(f'<span style="green:red">{obj.status}</span>')
        else:
            return obj.status

    def get_urls(self):
        urls = super().get_urls()
        date_urls = [
            path('date_view/', self.date_view)
        ]
        return date_urls + urls

    def date_view(self, request):
        week_date = datetime.datetime.now() - datetime.timedelta(days=3)
        week_data = Order.objects.filter(register_date__gte=week_date)
        data = Order.objects.filter(register_date__lt=week_date)

        context = dict(
            self.admin_site.each_context(request),
            week_data=week_data,
            data=data
        )
        return TemplateResponse(request, 'admin/order_date_view.html', context)

    styled_status.short_description = '상태'


admin.site.register(Order, OrderAdmin)
