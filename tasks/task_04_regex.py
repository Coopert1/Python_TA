import re


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.validate_password(password)

    @staticmethod
    def validate_password(password):
        if re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
            return password
        else:
            raise ValueError

    def update_password(self, new_password):
        self.password = self.validate_password(new_password)


