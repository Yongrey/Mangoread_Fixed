from rest_framework import serializers
from .models import Review
from rest_framework.exceptions import ValidationError




class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'manga', 'stars')