from django.test import TestCase
from myapp.bank import Bank
from myapp.models import Account, User
from mock import Mock, patch

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
        account = Account(account_no='HBJJJJ-4321')
        self.bank = Bank(user, account)

        self.assertFalse(self.bank.validate_account_number())

    def test_is_validate(self):
        bank = Mock(spec = Bank)
        mock_account = Mock(spec=Account)
        mock_account.account_no='HJ-8989'
        bank.account = mock_account
        bank_validate_method_patch_age = patch('myapp.bank.Bank.validate_age')
        bank_validate_method_mock =  bank_validate_method_patch_age.start()

        bank_validate_method_mock.return_value = True

        self.assertTrue(bank.validate_age_and_account())