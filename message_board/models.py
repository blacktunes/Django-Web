from django.db import models


class MessageBoard(models.Model):
    name = models.CharField(max_length=100, verbose_name="留言者")
    text = models.TextField(verbose_name="留言内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="留言时间")

    class Meta:
        verbose_name = u"留言"
        verbose_name_plural = u'留言'

    def __str__(self):
        return self.text