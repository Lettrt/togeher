from django.db import models
from django.contrib.auth.models import User
from news.models import News


# class News(models.Model):
#      pass 

class Comment(models.Model):
        user_id = models.ForeignKey(User, on_delete=models.CASCADE)
        news_id = models.ForeignKey(News, on_delete=models.CASCADE)
        body = models.TextField(max_length=2000)
        create_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            verbose_name = "Комментарий"
            verbose_name_plural = "Комментарии"

        def __str__(self):
            return self.body


#