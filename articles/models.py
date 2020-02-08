from django.db import models


class Article(models.Model):
    author_name = models.CharField('author', default='Somebody', max_length=32)
    title = models.CharField('title', default='Title', max_length=120)
    article_text = models.CharField('text', max_length=5000)
    publish_date = models.DateTimeField('date', auto_now_add=True)
    rating = models.IntegerField('rating', default=0)

    def __repr__(self):
        return self.article_text