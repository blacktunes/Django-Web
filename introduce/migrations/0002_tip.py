# Generated by Django 2.0.3 on 2018-04-16 08:21

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '提示',
                'verbose_name_plural': '提示',
            },
        ),
    ]
