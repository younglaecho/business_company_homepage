from django.contrib import admin

from .models import QandA
# Register your models here.

class QandAadmin(admin.ModelAdmin):
    list_display = ('title', 'writer') 

admin.site.register(QandA, QandAadmin)
