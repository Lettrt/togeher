
from django.db import models


class Profile(models.Model):
    news:models.ForeignKey("News",on_delete=models.CASCADE, related_name='news')
    username:models.OneToOneField("User",on_delete=models.CASCADE, related_name='name')
    comment:models.ForeignKey("Comment",on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return self.news
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"