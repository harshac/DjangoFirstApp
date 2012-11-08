from django.test import TestCase
from myapp.new_user_form import NewUserForm
from django.core.exceptions import ValidationError


class NewUserTest(TestCase):

    def test_new_user_should_be_valid(self):
        new_user_form = NewUserForm({'name':'test','age':10})
        self.assertTrue(new_user_form.is_valid())

    def test_new_user_should_be_binded(self):
        new_user_form = NewUserForm(initial = {'name' : 'test', 'age' : 10})
        #TODO: check how to bind a form with a dict
        self.assertFalse(new_user_form.is_bound)

    def test_new_user_should_require_name(self):
        new_user_form = NewUserForm({'age':10})
        form_is_valid = new_user_form.is_valid()
        self.assertFalse(form_is_valid)

    def test_new_user_should_not_require_age(self):
        new_user_form = NewUserForm({'name':'test'})
        form_is_valid = new_user_form.is_valid()
        self.assertTrue(form_is_valid)

    def test_new_user_name_should_not_be_greater_than_thirty(self):
        new_user_form = NewUserForm({'name':'abcdefghijklmnopqrstuvwxyzabcde'})
        form_is_valid = new_user_form.is_valid()
        self.assertFalse(form_is_valid)

    def test_new_user_age_should_not_be_less_than_equal_to_zero(self):
        new_user_form = NewUserForm({'name':'test', 'age':0})
#        self.assertRaises(ValidationError,new_user_form.is_valid())
        form_is_valid = new_user_form.is_valid()
#        self.assertEquals(str(type(new_user_form.cleaned_data['age'])),'foo')
        self.assertFalse(form_is_valid)

