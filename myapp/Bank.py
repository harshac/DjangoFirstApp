
class Bank(object):

    def __init__(self,user,account):
        self.user = user
        self.account = account

    def does_user_exists(self):
        return self.user.if_exists()

    def validate_age(self):
        return self.user.if_adult()

    def validate_account_number(self):
        return self.account.is_valid()

    def validate_age_and_account(self):
        return self.validate_account_number() and self.validate_age()