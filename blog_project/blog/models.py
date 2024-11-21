from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  categories = models.ManyToManyField('Category', related_name='posts')

  def __str__(self):
    return self.title
  
class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
  text = models.TextField()
  created_at = models.DateTimeField(default=now)

  def __str__(self):
    return f'Comment by {self.author} on {self.post}'
  
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name