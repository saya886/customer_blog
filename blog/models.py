from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
# Create your models here.


class blog_instance(models.Model):
    categary_choice = ( 
        ("BUSINESS STORY", "BUSINESS STORY"), 
        ("STUDENT VOICE", "STUDENT VOICE"), 
        ("CULTURAL ADVENTURE", "CULTURAL ADVENTURE"), 
    ) 
    title = models.TextField()
    author = models.TextField(default="")
    categary = models.CharField( 
        max_length = 200, 
        choices = categary_choice, 
        default = ''
        )
    blog_img = models.ImageField(upload_to ='uploads/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'/', height_field=None, width_field=None, max_length=1000,default="uploads/default_blog.png",help_text="图片的大小务必是342x215")
    content = RichTextUploadingField()
    
    push_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%d" % self.pk

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'  #保证取消admin的model的s

class program_instance(models.Model):

    title_1 = models.TextField()
    title_2 = models.TextField()
    desc = models.TextField(default="")

    program_img = models.ImageField(upload_to ='uploads/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'/', height_field=None, width_field=None, max_length=1000,default="uploads/default_program.png",help_text="")
    content = RichTextUploadingField(default="")

    learning_objectives = RichTextUploadingField(default="")
    ltinerary = RichTextUploadingField(default="")
    details = RichTextUploadingField(default="")

    push_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%d" % self.pk
        

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'  #保证取消admin的model的s

class testimonials_instance(models.Model):
    message = models.TextField(default="")
    img_src = models.ImageField(upload_to ='uploads/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'/', height_field=None, width_field=None, max_length=1000,default="uploads/default_program.png",help_text="")
    content = models.TextField(default="")

    def __str__(self):
        return "%d" % self.pk
        

    class Meta:
        verbose_name = '感言'
        verbose_name_plural = '感言'  #保证取消admin的model的s

class leave_comment(models.Model):
    name = models.TextField()
    mail_addr = models.TextField()
    phone = models.TextField()
    content = models.TextField()
    push_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%d" % self.pk

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言'  #保证取消admin的model的s