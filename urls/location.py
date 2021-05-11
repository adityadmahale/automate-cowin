from base import BASE_URL

LOCATION = "{}/admin/location".format(BASE_URL)
STATES_URL = "{}/states".format(LOCATION)


def get_districts_url(state_id):
    return "{}/districts/{}".format(LOCATION, state_id)