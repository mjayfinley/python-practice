class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.email)

    def greet_user(self):
        print(f"Hello {self.first_name}, how are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)


user_one = User("Micah", "Finley", 29, "mjayfinley@gmail.com")
user_one.describe_user()
user_one.greet_user()

user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()

user_one.reset_login_attempts()

# user_two = User("Samantha", "Finley", 28, "sam@gmail.com")
# user_two.describe_user()
# user_two.greet_user()

# user_three = User("Murphy", "Finley", 4, "murphy@gmail.com")
# user_three.describe_user()
# user_three.greet_user()
