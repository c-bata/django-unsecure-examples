from django.conf import settings
from django.db import models


class Comment(models.Model):
    content = models.CharField('本文', max_length=128)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者',
                                  on_delete=models.CASCADE)
