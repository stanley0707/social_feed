from rest_framework import serializers
from .models import VkUser


class FeedSerializer(serializers.ModelSerializer):
    """  Сериализуем полученные данные со страницы """
    
    class Meta:
        model = VkUser
        depth = 10
        field = ('__all__')
        