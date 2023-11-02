
from django.utils import timezone

from rest_framework import serializers

from .models import News


class NewsModelSerializer(serializers.ModelSerializer):

    update_at = serializers.DateTimeField(default=timezone.now)


    class Meta:
        model = News
        fields = '__all__'
