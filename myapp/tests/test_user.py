from django.test import TestCase
from myapp.models import User

class UserTest(TestCase):

    def test_if_user_does_not_exist(self):
        new_user = User(name='test', age=10)

        self.assertFalse(new_user.if_exists())


    def test_if_user_exists(self):
        new_user = User.objects.create(name='test',age=10)

        self.assertTrue(new_user.if_exists())


    def test_if_user_age_is_less_than_eighteen(self):
        new_user = User(name='test', age=17)

        self.assertFalse(new_user.if_adult())


