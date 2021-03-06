from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
import re

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def if_exists(self):
        flag = True
        try:
            User.objects.get(name = self.name)

        except ObjectDoesNotExist:
            flag = False

        return flag


    def if_adult(self):
        if self.age < 18:
            return False

        return True


    def __unicode__(self):
        return self.name

class Account(models.Model):
    account_no = models.CharField(max_length=7)
    user = models.ForeignKey('User')

    def is_valid(self):
       return re.match(r"[A-Z][A-Z]-\d+$",self.account_no) != None


