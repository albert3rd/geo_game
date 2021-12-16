from django.db import models
import geocoder
import requests
import os

# Create your models here.

class Answers(models.Model):
    user_latitude = models.FloatField(blank=True)
    user_longitude = models.FloatField(blank=True)
    user_answer = models.TextField()

    def answer_return(self, *args, **kwargs):
        g = geocoder.mapbox(self.user_answer, key=os.environ.get("MAPBOX_API_KEY"))
        self.user_latitude = g.latlng[0]
        self.user_longitude = g.latlng[1]
        return super(Answers, self).answer_return(*args, **kwargs)


class Trivia_Questions(models.Model):
    user_answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    trivia_question = models.TextField()
    correct_answer = models.TextField()
    correct_longitude = models.FloatField(blank=True)
    correct_latitude = models.FloatField(blank=True)
