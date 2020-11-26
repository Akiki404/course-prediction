from django.db import models


# Create your models here.
class Record(models.Model):
    gender = models.CharField(max_length=20)
    grade = models.IntegerField()
    openness = models.IntegerField()
    agreeableness = models.IntegerField()
    emotions = models.IntegerField()
    conscientiousness = models.IntegerField()
    extraversion = models.IntegerField()
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.course