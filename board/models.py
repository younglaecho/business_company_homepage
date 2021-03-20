from django.db import models
# Create your models here.

class Noticeboard(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목',
                             default='some string')
    contents = models.TextField(verbose_name='내용',
                                default='some content')
    writer = models.ForeignKey('company_user.Comuser', on_delete=models.CASCADE,
                                 verbose_name='작성자') # on_delete= models.CASCADE : ForeignKey 에 해당하는 데이터가 삭제되면 같이 삭제
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    post_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta: # 테이블 이름 정하기
        db_table = 'com_notice_board'
        verbose_name = '공지사항 게시글'
        verbose_name_plural = '공지사항 게시글'

    @property
    def update_counter(self):
        self.post_hit += 1
        self.save()

    
class Referenceboard(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목',
                             default='some string')
    contents = models.TextField(verbose_name='내용',
                                default='some content')
    writer = models.ForeignKey('company_user.Comuser', on_delete=models.CASCADE,
                                 verbose_name='작성자') # on_delete= models.CASCADE : ForeignKey 에 해당하는 데이터가 삭제되면 같이 삭제
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    post_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta: # 테이블 이름 정하기
        db_table = 'com_reference_board'
        verbose_name = '자료실 게시글'
        verbose_name_plural = '자료실 게시글'

    @property
    def update_counter(self):
        self.post_hit += 1
        self.save()

class Comment(models.Model):
    author = models.CharField(max_length=128,
                             verbose_name='작성자')
    password = models.CharField(max_length=128,
                                verbose_name='비밀번호')
    content = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField()
    notice_comment = models.ForeignKey(Noticeboard, 
                                       related_name='comments',
                                       null=True,
                                       blank=True, 
                                       on_delete=models.CASCADE)
    reference_comment = models.ForeignKey(Referenceboard, 
                                          null=True,
                                          blank=True, 
                                          on_delete=models.CASCADE)
            
    def __str__(self):
        return self.author

    class Meta: # 테이블 이름 정하기
        db_table = 'com_comment'
        verbose_name = '게시판 댓글'
        verbose_name_plural = '게시판 댓글'