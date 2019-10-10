from django.contrib.admin import AdminSite
from django.contrib import admin
from blog.models import *
# Register your models here.

class blog_instance_admin(admin.ModelAdmin):
    list_display = ['title', 'content', 'push_time']

class leave_comment_admin(admin.ModelAdmin):
    list_display = ['name', 'mail_addr', 'phone','content','push_time']


class MyAdminSite(AdminSite):
    site_header = 'Administration Manage System'
    site_title = "Administration Manage System"

admin_site = MyAdminSite(name='myadmin')
admin_site.register(blog_instance,blog_instance_admin)
admin_site.register(leave_comment,leave_comment_admin)