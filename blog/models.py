from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    #class CharField(max_length=None, **options)
    title = models.CharField(max_length=200)
    #class ForeignKey(to, on_delete, **options)
    author = models.ForeignKey(
      'auth.User',
      on_delete = models.CASCADE, #CASCADE/PROTECT/RESTRICT
    )
    #class TextField(**options)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args = [str(self.id)])
