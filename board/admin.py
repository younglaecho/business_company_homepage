from django.contrib import admin

# Register your models here.
from .models import Board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer','post_type') # 어드민 페이지에서 출력하고 싶은 필드를 설정


admin.site.register(Board, BoardAdmin)