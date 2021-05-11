import sys
import http

from urls import auth as auth_urls
from hashlib import sha256


class Auth:

    def __init__(self, number):
        self.number = number

    def get_token(self):
        txn_id = self._get_txn_id()
        return self._confirm_otp(txn_id)

    def _get_txn_id(self):
        status_code, response = http.post(
            auth_urls.GENERATE_OTP,
            json={"mobile": self.number}
        )
        if status_code != 200:
            print("OTP already sent")
            sys.exit()
        return response["txnId"]

    def _confirm_otp(self, txn_id):
        otp = str(input("Enter OTP: "))
        hashed_otp = sha256(otp).hexdigest()
        status_code, response = http.post(
            auth_urls.CONFIRM_OTP,
            json={
                "otp": hashed_otp,
                "txnId": txn_id
            }
        )
        if status_code == 200:
            return response["token"]
        sys.exit()
