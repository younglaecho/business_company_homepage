from django.contrib import admin
from .models import Comuser
# Register your models here.

class companyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password','registered_dttm') # 어드민 페이지에서 출력하고 싶은 필드를 설정


admin.site.register(Comuser, companyUserAdmin)