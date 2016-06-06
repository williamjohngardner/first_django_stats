from django.db import models


class BattingAvg(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    games = models.FloatField()
    at_bats = models.FloatField()
    runs = models.FloatField()
    hits = models.FloatField()
    doubles = models.FloatField()
    triples = models.FloatField()
    home_runs = models.FloatField()
    rbi = models.FloatField()
    strike_outs = models.FloatField()
    average = models.FloatField()

    def __str__(self):
        return self.name
