from django.db import models


# Create your models here.
class Record(models.Model):
    gender = models.CharField(max_length=20)
    grade = models.IntegerField()
    openness = models.FloatField()
    agreeableness = models.FloatField()
    emotions = models.FloatField()
    conscientiousness = models.FloatField()
    extraversion = models.FloatField()
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.course