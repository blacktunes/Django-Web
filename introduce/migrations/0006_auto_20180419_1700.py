# Generated by Django 2.0.3 on 2018-04-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduce', '0005_gamename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='introduce.GameName', verbose_name='游戏名'),
        ),
        migrations.AlterField(
            model_name='gamename',
            name='name',
            field=models.CharField(max_length=200, verbose_name='游戏名'),
        ),
    ]