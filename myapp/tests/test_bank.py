from django.test import TestCase
from myapp.Bank import Bank
from myapp.models import Account, User
from mock import Mock

class BankTest(TestCase):

#        account = Account(account_no='HJ-9099',user = accountHolder)

    def test_does_user_exists(self):
        accountHolder = User.objects.create(name='test',age=17)
        account = Mock(spec = Account)
        self.bank = Bank(accountHolder,account)

        self.assertTrue(self.bank.does_user_exists())

    def test_is_user_adult(self):
        user = Mock(spec = User)
        user.age = 21
        account = Mock(spec = Account)
        self.bank = Bank(user, account)

        self.assertTrue(self.bank.validate_age())

    def test_is_valid_account(self):
        user = Mock(spec = User)
        account = Mock(spec = Account)
        account.account_no = 'HB-4321'
        self.bank = Bank(user, account)

        self.assertTrue(self.bank.validate_account_number())
