from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class GameName(models.Model):
    name = models.CharField(max_length=200, verbose_name="游戏名")

    class Meta:
        verbose_name = u"游戏名"
        verbose_name_plural = u"游戏名"

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.ForeignKey(GameName, on_delete=models.CASCADE, null=True, verbose_name="游戏名")
    text = RichTextUploadingField(verbose_name="正文")

    class Meta:
        verbose_name = u"游戏介绍"
        verbose_name_plural = u"游戏介绍"


class UpdateLog(models.Model):
    text = RichTextUploadingField(verbose_name="内容")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

    class Meta:
        verbose_name = u"更新日志"
        verbose_name_plural = u"更新日志"


class Tip(models.Model):
    text = RichTextUploadingField(verbose_name="内容")

    class Meta:
        verbose_name = u"提示"
        verbose_name_plural = u"提示"
