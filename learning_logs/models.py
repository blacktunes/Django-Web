from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Topic(models.Model):
    text = models.CharField(max_length=200, verbose_name="主题名称")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建者")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = u"主题"

    def __str__(self):
        return self.text


class Entry(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="标题")
    text = RichTextUploadingField(verbose_name="内容")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="所属主题")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="创建者")

    class Meta:
        verbose_name = u"内容"
        verbose_name_plural = u'内容'

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text