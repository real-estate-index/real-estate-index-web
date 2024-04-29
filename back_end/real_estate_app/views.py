from django.shortcuts import render
from .models import Index, Region, News, Issue
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import IndexSerializer, RegionSerializer, NewsSerializer, IssueSerializer

@api_view(['GET'])
def index_view(request):
    indexes = Index.objects.all()
    serializer = IndexSerializer(indexes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def region_view(request):
    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def news_view(request):
    news_items = News.objects.all()
    serializer = NewsSerializer(news_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def issue_view(request):
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)