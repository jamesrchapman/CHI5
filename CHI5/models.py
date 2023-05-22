from django.db import models

class AptitudeTestData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    personality = models.CharField(max_length=100)
    intellectual_aptitude = models.IntegerField()
    love_connection = models.IntegerField()
    esteem_social_contribution = models.IntegerField()
    intellectual_interest = models.IntegerField()
    simple_pleasures = models.IntegerField()
    physical_engagement = models.IntegerField()