from django.contrib import admin
from .models import Fcuser
# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

    def changelist_view(self, request, extra_context=None):
        # 우리가 원하는 동작
        extra_context = {'title': '사용자 목록'}
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        fcuser = Fcuser.objects.get(pk=object_id)
        extra_context = {'title': f'{fcuser.email} 수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)


admin.site.register(Fcuser, FcuserAdmin)
admin.site.site_header = '고려화학 어드민'
admin.site.index_title = '고려화학매트'
admin.site.site_title = '고려화학매트'
