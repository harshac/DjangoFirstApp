from django import forms
from django.core.exceptions import ValidationError
class NewUserForm(forms.Form):
    name = forms.CharField(max_length = 30)
    age = forms.IntegerField(required = False)

    def clean_age(self):
        value = self.cleaned_data['age']
        print "******************\n"
        print value

        if value == 0 :
            raise ValidationError('You have entered invalid age')
        return value