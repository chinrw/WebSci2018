#!/usr/bin/env python

import json
from pprint import pprint
from urllib import request


class Authorizer(object):
    def __init__(self):
        """
        Initialize Authorizer object from file from data.
        """
        self.__weather_key = '3dfa9f9c19a712ac'

    def get_weather_key(self):
        return self.__weather_key


class CitySearchError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def get_weather_data(api_key, request_type, location):
    # return a dict data that contains required information
    url = 'http://api.wunderground.com/api/%s/%s/q/%s.json' \
          % (api_key, request_type, location)
    req = request.urlopen(url)
    data = json.loads(req.read())
    pprint(data)
    return data


def format_weather_data(json_data):
    if 'current_observation' in json_data:
        data = {'location': json_data["current_observation"]["display_location"]["full"],
                'weather': json_data["current_observation"]["weather"],
                'windchill': json_data["current_observation"]['windchill_string'],
                'temperature': json_data["current_observation"]['temperature_string'],
                'time': json_data["current_observation"]["observation_time"],
                'wind': json_data["current_observation"]["wind_string"],
                'humid': json_data["current_observation"]["relative_humidity"],
                'icon_url': json_data["current_observation"]["icon_url"],
                'forecast_url': json_data["current_observation"]["forecast_url"]}
        return data
    else:
        raise CitySearchError('No cities match your search query')


def from_lat_long(latitude, longitude, query_parameter='conditions'):
    location = latitude + ',' + longitude
    return format_weather_data(get_weather_data(Authorizer().get_weather_key(), query_parameter, location))
