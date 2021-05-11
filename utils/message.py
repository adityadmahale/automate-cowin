import json
import sys
from twilio.rest import Client


class Message:

    def __init__(self):
        self.client = Client()
        self.from_number, self.to_number = self._parse_number()

    def send_message(self, message):
        self.client.messages.create(
            to=self.to_number, from_=self.from_number, body=message
        )

    def _parse_number(self):
        with open("sms.json") as f:
            sms = json.load(f)
        if not (sms["from"] and sms["to"]):
            print("Fill numbers in the sms.json file.")
            sys.exit()
        return sms["from"], sms["to"]
