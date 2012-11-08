from django.test import TestCase
from myapp.models import *

class AccountTest(TestCase):

    def setUp(self):
        self.new_user = User.objects.create(name='test', age=10)

    def test_if_account_no_is_valid(self):
        account = Account(account_no='HB-1234', user = self.new_user)

        self.assertTrue(account.is_valid())

    def test_if_account_no_is_invalid(self):
        account = Account(account_no='HBA-1234', user = self.new_user)

        self.assertFalse(account.is_valid())


