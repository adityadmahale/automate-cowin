import sys

from datetime import timedelta, datetime


def get_date(day):
    if not day:
        day = raw_input("Slots(today/tomorrow): ")
    day = day.strip().lower()
    if day not in ["today", "tomorrow"]:
        print("Incorrect input")
        sys.exit()

    date = datetime.now()
    if day == "tomorrow":
        date = date + timedelta(days=1)
    return date.strftime('%d-%m-%y')


def get_iterations(time):
    if not time:
        while True:
            time = int(input("Script running time(1-24 hours): "))
            if 0 < time <= 24:
                break
    return (int(time) * 60 * 60) / 5


def get_pincode():
    pincode = raw_input("Enter pincode: ")
    return pincode
