from rest_framework import viewsets

from .models import News
from .serializers import NewsModelSerializer

class ViewsSetNews(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
