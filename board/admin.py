from django.contrib import admin

# Register your models here.
from .models import Noticeboard, Referenceboard, Comment
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer') # 어드민 페이지에서 출력하고 싶은 필드를 설정


admin.site.register(Noticeboard, BoardAdmin)
admin.site.register(Referenceboard, BoardAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_date')

admin.site.register(Comment, CommentAdmin)