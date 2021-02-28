from django.db import models
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목',
                             default='some string')
    contents = models.TextField(verbose_name='내용',
                                default='some content')
    writer = models.ForeignKey('company_user.Comuser', on_delete=models.CASCADE,
                                 verbose_name='작성자') # on_delete= models.CASCADE : ForeignKey 에 해당하는 데이터가 삭제되면 같이 삭제
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    post_type = models.CharField(max_length=32, 
                                verbose_name='게시물 종류')

    def __str__(self):
        return self.title

    class Meta: # 테이블 이름 정하기
        db_table = 'com_board'
        verbose_name = 'com 게시글'
        verbose_name_plural = 'com 게시글'