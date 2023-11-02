from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=2000)
    img = models.ImageField(upload_to='news/', null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=datetime.now())
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
