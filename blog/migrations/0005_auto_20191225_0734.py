# Generated by Django 3.0.1 on 2019-12-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_instance_categary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_instance',
            name='categary',
            field=models.CharField(choices=[('BUSINESS STORY', 'BUSINESS STORY'), ('STUDENT VOICE', 'STUDENT VOICE'), ('CULTURAL ADVENTURE', 'CULTURAL ADVENTURE')], default='BUSINESS STORY', max_length=200),
        ),
    ]
