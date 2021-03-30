from django.db import models

# Create your models here.

# class Board(models.Model):
#     writer = models.CharField(max_length=128,
#                              verbose_name='작성자')
#     cmapany = models.CharField(max_length=128,
#                                verbose_name='회사명')
#     email = models.CharField(max_length=128,
#                                verbose_name='이메일')
#     phone = models.CharField(verbose_name='전화번호')
#     fax = models.CharField(verbose_name='팩스번호')
#     title = models.CharField(max_length=128,
#                              verbose_name='제목')
#     content = models.TextField(verbose_name='내용',
#                                 default='some content')

#     def __str__(self):
#         return self.title

#     class Meta: # 테이블 이름 정하기
#         db_table = 'death_board'
#         verbose_name = 'death 게시글'
#         verbose_name_plural = 'death 게시글'