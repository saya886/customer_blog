from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class blog_instance(models.Model):
    title = models.TextField()
    content = RichTextUploadingField()
    push_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%d" % self.pk

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'  #保证取消admin的model的s

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