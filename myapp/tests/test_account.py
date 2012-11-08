from django.test import TestCase
from myapp.models import *


class AccountTest(TestCase):

    def setUp(self):
        self.real_user = User.objects.create(name='foo',age=12)

    def test_if_account_no_is_valid(self):
        account = Account(account_no='HB-1234', user = self.real_user)

        self.assertTrue(account.is_valid())

    def test_if_account_no_is_invalid(self):
        account = Account(account_no='HBA-1234', user = self.real_user)

        self.assertFalse(account.is_valid())


