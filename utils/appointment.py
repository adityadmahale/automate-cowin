import http
import time

from urls import appointment
from message import Message


def find_by_district(district_id, date):
    url = appointment.get_by_district_url(district_id, date)
    return http.get(url)


def find_by_pin(pincode, date):
    url = appointment.get_by_pin_url(pincode, date)
    return http.get(url)


def find_slots(date, criteria, criteria_value, iterations):
    message = Message()
    print("Searching for slots on {}".format(date))
    for i in range(iterations):
        if criteria == "district":
            status, response = find_by_district(criteria_value, date)
        else:
            status, response = find_by_pin(criteria_value, date)

        if status != 200:
            time.sleep(5)
            continue

        sessions = response["sessions"]
        if sessions:
            codes = " ".join([str(session["pincode"]) for session in sessions])
            notification = "Vaccination slots are available at the following pin codes: {}".format(codes)
            print(notification)
            message.send_message(notification)
            break
        time.sleep(5)
    else:
        print("Slots not found.")
