from base import BASE_URL

BASE = "{}/appointment/sessions/public".format(BASE_URL)


def get_by_district_url(district_id, date):
    return "{}/findByDistrict?district_id={}&date={}".format(BASE, district_id, date)


def get_by_pin_url(pincode, date):
    return "{}/findByPin?pincode={}&date={}".format(BASE, pincode, date)
