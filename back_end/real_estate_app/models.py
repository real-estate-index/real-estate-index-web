from django.db import models

# 뉴스 조회
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

# 정부 이슈 조회
class Issue(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

# 지역 조회
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 지역별 구 조회
class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 지역별 Fear & Greed Index 저장
class DistrictIndex(models.Model):
    district = models.ForeignKey(District, related_name='indexes', on_delete=models.CASCADE)
    index_value = models.FloatField()

    class Meta:
        db_table = 'real_estate_app_fear_greed_index'

    def __str__(self):
        return f"{self.district.name}: {self.index_value}"

# 지역별 심리지수 저장
class SentimentIndex(models.Model):
    district = models.ForeignKey(District, related_name='sentiment_indexes', on_delete=models.CASCADE)
    year_month = models.CharField(max_length=6)  # 'YYYYMM' 형식
    index_value = models.FloatField()

    class Meta:
        db_table = 'real_estate_app_sentiment_index'
        unique_together = ('district', 'year_month')

    def __str__(self):
        return f"{self.district.name} - {self.year_month}: {self.index_value}"

# 지역별 평당 거래가 저장
class TradePrice(models.Model):
    district = models.ForeignKey(District, related_name='trade_prices', on_delete=models.CASCADE)
    year_month = models.CharField(max_length=6)  # 'YYYYMM' 형식
    price = models.FloatField()

    class Meta:
        db_table = 'real_estate_app_trade_price'
        unique_together = ('district', 'year_month')

    def __str__(self):
        return f"{self.district.name} - {self.year_month}: {self.price}"

# 지역별 거래량 저장
class TradeAmount(models.Model):
    district = models.ForeignKey(District, related_name='trade_amounts', on_delete=models.CASCADE)
    year_month = models.CharField(max_length=6)  # 'YYYYMM' 형식
    amount = models.FloatField()

    class Meta:
        db_table = 'real_estate_app_trade_amount'
        unique_together = ('district', 'year_month')

    def __str__(self):
        return f"{self.district.name} - {self.year_month}: {self.amount}"

# 지역별 모멘텀 저장
class Momentum(models.Model):
    district = models.ForeignKey(District, related_name='momentums', on_delete=models.CASCADE)
    year_month = models.CharField(max_length=6)  # 'YYYYMM' 형식
    momentum = models.FloatField()

    class Meta:
        db_table = 'real_estate_app_momentum'
        unique_together = ('district', 'year_month')

    def __str__(self):
        return f"{self.district.name} - {self.year_month}: {self.momentum}"
