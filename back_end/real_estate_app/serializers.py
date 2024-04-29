from rest_framework import serializers
from .models import Index, Region, News, Issue

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['region', 'value']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'content']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'content']