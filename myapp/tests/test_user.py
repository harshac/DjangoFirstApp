from django.test import TestCase
from myapp.models import User
from mock import Mock,patch

class UserTest(TestCase):

    def setUp(self):
        self.new_user = User(name='test', age=10)
        self.new_user_if_exists_patcher = patch('myapp.models.User.if_exists')
        self.new_user_if_exists_mock = self.new_user_if_exists_patcher.start()

    def test_if_user_does_not_exist(self):
        self.new_user_if_exists_mock.return_value = False

        self.assertFalse(self.new_user.if_exists())


    def test_if_user_exists(self):
        new_user = User.objects.create(name='test',age=10)

        self.assertTrue(new_user.if_exists())


    def test_if_user_age_is_less_than_eighteen(self):
        new_user = User(name='test', age=17)

        self.assertFalse(new_user.if_adult())

    def tearDown(self):
        self.new_user_if_exists_patcher.stop()

