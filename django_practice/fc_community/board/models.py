from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE ,verbose_name="작성자")
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    # 내가 테이플 이름을 정하고 싶으면 이렇게 쓰면 됨
    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '고려화학매트 게시글'
        verbose_name_plural = '고려화학매트 게시글'