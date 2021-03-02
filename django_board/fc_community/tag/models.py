from django.db import models

# Create your models here.

class Tag(models.Model):
  name = models.CharField(max_length=32, verbose_name = '태그명')
  registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

  def __str__(self):
        return self.name

    # 내가 테이플 이름을 정하고 싶으면 이렇게 쓰면 됨
  class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '고려화학매트 태그'
        verbose_name_plural = '고려화학매트 태그'