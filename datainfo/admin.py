from django.contrib import admin
from .models import User,Blog,BlogComments
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','mobile_number','user_info']
    list_filter = ['user_name']
    search_fields = ['user_name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','blog_description','created_on','updated_on']
    list_filter = ['title']
    search_fields = ['id','user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','user','blog','comment']
    list_filter=['comment','user']
    search_fields = ['blog']


admin.site.register(User,UserAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComments,CommentAdmin)