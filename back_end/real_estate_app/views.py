from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News, Issue, Region, District, DistrictIndex, SentimentIndex, TradePrice, TradeAmount, Momentum

@api_view(['GET'])
def fear_greed_index(request):
    district_id = request.query_params.get('districtId')
    if district_id:
        try:
            district_indexes = DistrictIndex.objects.filter(district_id=district_id).values('id', 'district_id', 'index_value')
            data = [{'id': index['id'], 'district_id': index['district_id'], 'index_value': index['index_value']} for index in district_indexes]
            return Response(data)
        except Exception as e:
            print(f"Error fetching fear_greed_index for district_id {district_id}: {str(e)}")
            return Response({'error': str(e)}, status=500)
    return Response({'error': 'districtId is required'}, status=400)

@api_view(['GET'])
def news_and_issues(request):
    news_items = News.objects.all().values()
    issues_items = Issue.objects.all().values()
    data = {'news': list(news_items), 'issues': list(issues_items)}
    return Response(data)

@api_view(['GET'])
def region_districts(request):
    region_id = request.query_params.get('regionId')
    if region_id:
        try:
            region = Region.objects.filter(id=region_id).first()
            if region:
                districts = District.objects.filter(region=region).values('id', 'name')
                return Response(list(districts))
            else:
                return Response({'error': 'Region not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    return Response({'error': 'regionId is required'}, status=400)

@api_view(['GET'])
def sentiment_index(request):
    district_id = request.query_params.get('district_id')
    if district_id:
        try:
            indices = SentimentIndex.objects.filter(district_id=district_id).values('year_month', 'index_value')
            data = [{'year_month': index['year_month'], 'index_value': index['index_value']} for index in indices]
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    return Response({'error': 'district_id is required'}, status=400)

@api_view(['GET'])
def trade_price(request):
    district_id = request.query_params.get('district_id')
    if district_id:
        try:
            prices = TradePrice.objects.filter(district_id=district_id).values('year_month', 'price')
            data = [{'year_month': price['year_month'], 'price': price['price']} for price in prices]
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    return Response({'error': 'district_id is required'}, status=400)

@api_view(['GET'])
def trade_amount(request):
    district_id = request.query_params.get('district_id')
    if district_id:
        try:
            amounts = TradeAmount.objects.filter(district_id=district_id).values('year_month', 'amount')
            data = [{'year_month': amount['year_month'], 'amount': amount['amount']} for amount in amounts]
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    return Response({'error': 'district_id is required'}, status=400)

@api_view(['GET'])
def momentum(request):
    district_id = request.query_params.get('district_id')
    if district_id:
        try:
            momenta = Momentum.objects.filter(district_id=district_id).values('year_month', 'momentum')
            data = [{'year_month': momentum['year_month'], 'momentum': momentum['momentum']} for momentum in momenta]
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    return Response({'error': 'district_id is required'}, status=400)
