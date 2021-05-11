from base import BASE_URL

AUTH_URL = "{}/auth".format(BASE_URL)
GENERATE_OTP = "{}/public/generateOTP".format(AUTH_URL)
CONFIRM_OTP = "{}/public/confirmOTP".format(AUTH_URL)
