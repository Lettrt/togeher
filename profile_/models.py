from django.db import models
from news.models import News
from django.contrib.auth.models import User


class Profile(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE, related_name='news')
    username = models.OneToOneField(User,on_delete=models.CASCADE, related_name='name')

    def __str__(self) -> str:
        return self.news
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"