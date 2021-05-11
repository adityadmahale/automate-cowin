# Find slots by district
import sys

from utils import appointment, utils
from utils.location import Location


def find_slots_by_district():
    state, district, day, time = args if len(args) == 4 else ("", "", "", "")
    location = Location(state, district)
    state_id = location.get_state_id()
    district_id = location.get_district_id(state_id)
    date = utils.get_date(day)
    iterations = utils.get_iterations(time)
    appointment.find_slots(date, "district", district_id, iterations)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 0 and len(args) != 4:
        print("Pass four arguments in the following order:"
              " 1. state 2. district 3. day(today/tomorrow) 4. Script duration(1-24)")
        sys.exit()
    find_slots_by_district()
