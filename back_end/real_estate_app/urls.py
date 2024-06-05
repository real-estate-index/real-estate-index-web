from django.urls import path
from .views import fear_greed_index, news_and_issues, region_districts, sentiment_index, trade_price, trade_amount, momentum

urlpatterns = [
    path('api/fear_greed_index/', fear_greed_index, name='fear_greed_index'),
    path('api/news_and_issues/', news_and_issues, name='news_and_issues'),
    path('api/region_districts/', region_districts, name='region_districts'),
    path('api/sentiment_index/', sentiment_index, name='sentiment_index'),
    path('api/trade_price/', trade_price, name='trade_price'),
    path('api/trade_amount/', trade_amount, name='trade_amount'),
    path('api/momentum/', momentum, name='momentum'),
]
