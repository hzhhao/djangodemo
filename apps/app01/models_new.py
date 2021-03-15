from django.db import models

class App01Result(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    class Meta:
        verbose_name = '测试模型'

        verbose_name_plural = verbose_name
