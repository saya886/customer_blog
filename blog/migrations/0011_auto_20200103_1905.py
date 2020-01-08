# Generated by Django 2.1.7 on 2020-01-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200103_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonials_instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
                ('img_src', models.ImageField(default='uploads/default_program.png', max_length=1000, upload_to='uploads/20200103190550/')),
                ('content', models.TextField(default='')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.AlterField(
            model_name='blog_instance',
            name='blog_img',
            field=models.ImageField(default='uploads/default_blog.png', help_text='图片的大小务必是342x215', max_length=1000, upload_to='uploads/20200103190550/'),
        ),
        migrations.AlterField(
            model_name='program_instance',
            name='program_img',
            field=models.ImageField(default='uploads/default_program.png', max_length=1000, upload_to='uploads/20200103190550/'),
        ),
    ]