from django.db import models

# Create your models here.

class QandA(models.Model):
    writer = models.CharField(max_length=128,
                             verbose_name='작성자')
    company = models.CharField(max_length=256,
                               verbose_name='회사명')
    email = models.CharField(max_length=256,
                               verbose_name='이메일')
    phone = models.CharField(max_length=256,
                             verbose_name='전화번호')
    fax = models.CharField(max_length=256, 
                           verbose_name='팩스번호')
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    register_dttm = models.DateTimeField(auto_now_add=True,
                                         verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta: # 테이블 이름 정하기
        db_table = '문의사항'
        verbose_name = '문의사항'
        verbose_name_plural = '문의사항'