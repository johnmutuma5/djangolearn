from django.db import models

from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=25)
  body = models.TextField()
  author_id = models.IntegerField()


  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def __str__(self):
    return self.title
