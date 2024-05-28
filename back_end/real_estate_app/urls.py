from django.urls import path
from . import views

urlpatterns = [
    path('api/fear-greed-index', views.fear_greed_index, name='fear-greed-index'),
    path('api/news-and-issues/', views.news_and_issues, name='news-and-issues')
]
