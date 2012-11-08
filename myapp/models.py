from django.db import models
from django.forms import ModelForm
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

