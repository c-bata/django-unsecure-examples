from django.db import models


class Snippet(models.Model):
    title = models.CharField('タイトル', max_length=128)

    class Meta:
        db_table = 'snippets'
