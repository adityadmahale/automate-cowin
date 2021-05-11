import sys
import http

from urls.location import STATES_URL, get_districts_url


class Location:

    def __init__(self, state, district):
        self.state = state
        self.district = district

    def get_state_id(self):
        return self._get_id("state", STATES_URL)

    def get_district_id(self, state_id):
        url = get_districts_url(state_id)
        return self._get_id("district", url)

    def _get_id(self, value, url):
        status_code, response = http.get(url)
        if status_code != 200:
            print("API server is not reachable.")
            sys.exit()

        if value == "district" and self.district:
            entered_value = self.district
        elif value == "state" and self.state:
            entered_value = self.state
        else:
            for i, key in enumerate(response["{}s".format(value)]):
                print("{}. {}".format(i + 1, key["{}_name".format(value)]))
            entered_value = raw_input("Enter {}: ".format(value))

        entered_value = entered_value.title().strip()

        for district in response["{}s".format(value)]:
            if district["{}_name".format(value)] == entered_value:
                return district["{}_id".format(value)]
        print("{} not found.".format(value.title()))
        sys.exit()
