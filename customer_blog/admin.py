from django.contrib.admin import AdminSite
from django.contrib import admin
from blog.models import *
# Register your models here.

class blog_instance_admin(admin.ModelAdmin):
    list_display = ['title', 'author','push_time']

class program_instance_admin(admin.ModelAdmin):
    list_display = ['title_1', 'title_2', 'push_time']

class leave_comment_admin(admin.ModelAdmin):
    list_display = ['name', 'mail_addr', 'phone','content','push_time']


class MyAdminSite(AdminSite):
    site_header = 'Manage System'
    site_title = "Manage System"

admin_site = MyAdminSite(name='myadmin')
admin_site.register(blog_instance,blog_instance_admin)
admin_site.register(leave_comment,leave_comment_admin)
admin_site.register(program_instance,program_instance_admin)