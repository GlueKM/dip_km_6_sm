import data
import configuration
import requests


def post_new_order():
     return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                             json=data.CREATE_ORDER_BODY)


def get_order_by_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + track_number)

