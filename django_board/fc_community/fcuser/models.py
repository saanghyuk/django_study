from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=64, verbose_name="사용자명")
    useremail = models.EmailField(max_length=128, verbose_name="사용자이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    # 내가 테이플 이름을 정하고 싶으면 이렇게 쓰면 됨
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '고려화학매트 사용자'
        verbose_name_plural = '고려화학매트 사용자'