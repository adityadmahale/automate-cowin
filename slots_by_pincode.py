# Find slots by pincode
import sys

from utils import appointment, utils


def get_slots_by_pincode():
    pincode, day, time = args if len(args) == 3 else ("", "", "")
    pincode = pincode if pincode else utils.get_pincode()
    date = utils.get_date(day)
    iterations = utils.get_iterations(time)
    appointment.find_slots(date, "pincode", pincode, iterations)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 0 and len(args) != 3:
        print("Pass three arguments in the following order:"
              " 1. pincode 2. day(today/tomorrow) 3. Script duration(1-24)")
        sys.exit()
    get_slots_by_pincode()
