from django.db import models
from news.models import News
from django.contrib.auth.models import User
from comments.models import Comment

class Profile(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE, related_name='news')
    username = models.OneToOneField(User,on_delete=models.CASCADE, related_name='name')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return self.news
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"