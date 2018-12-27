from django.contrib import admin
from .models import Article,Column
# Register your models here.

# 选择要列出的字段
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name','slug','summary','nav_display','home_display')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','pub_date','update_time')

# 注册模型
admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)

