# Generated by Django 2.1.7 on 2020-02-13 06:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200103_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonials_instance',
            options={'verbose_name': '感言', 'verbose_name_plural': '感言'},
        ),
        migrations.AddField(
            model_name='program_instance',
            name='content_cn',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AddField(
            model_name='program_instance',
            name='desc_cn',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='program_instance',
            name='details_cn',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AddField(
            model_name='program_instance',
            name='learning_objectives_cn',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AddField(
            model_name='program_instance',
            name='ltinerary_cn',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AddField(
            model_name='program_instance',
            name='title_1_cn',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='program_instance',
            name='title_2_cn',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog_instance',
            name='blog_img',
            field=models.ImageField(default='uploads/default_blog.png', help_text='图片的大小务必是342x215', max_length=1000, upload_to='uploads/20200213140929/'),
        ),
        migrations.AlterField(
            model_name='program_instance',
            name='program_img',
            field=models.ImageField(default='uploads/default_program.png', max_length=1000, upload_to='uploads/20200213140929/'),
        ),
        migrations.AlterField(
            model_name='program_instance',
            name='title_1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='program_instance',
            name='title_2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='testimonials_instance',
            name='img_src',
            field=models.ImageField(default='uploads/default_program.png', max_length=1000, upload_to='uploads/20200213140929/'),
        ),
    ]
