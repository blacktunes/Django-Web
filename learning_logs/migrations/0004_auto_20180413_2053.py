# Generated by Django 2.0.4 on 2018-04-13 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': '内容', 'verbose_name_plural': '内容'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': '主题', 'verbose_name_plural': '主题'},
        ),
    ]