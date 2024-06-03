from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News, Issue, Region, District
from .utils import calculate, news_api

@api_view(['GET'])
def fear_greed_index(request):
    value_item = calculate()
    return Response({'value_item':value_item})

@api_view(['GET'])
def news_and_issues(request):
    news_items = News.objects.all().values()
    issues_items = Issue.objects.all().values()
    data = {'news':list(news_items), 'issues':list(issues_items)}
    return Response(data)

@api_view(['GET'])
def region_districts(request):
    region_id = request.query_params.get('regionId')
    if region_id:
        region = Region.objects.filter(id=region_id).first()
        if region:
            districts = District.objects.filter(region=region).values('id', 'name')
            return Response(list(districts))
        return Response({'error': 'Region not found'}, status=404)
    return Response({'error': 'regionId is required'}, status=400)