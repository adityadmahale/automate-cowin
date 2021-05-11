# Authentication
from utils.auth import Auth

number = input("Enter mobile number: ")
mobile = Auth(number)
token = mobile.get_token()
print(token)
