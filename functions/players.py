# -*- coding: utf-8 -*-
"""
Getting player information from the FPL database
"""
from simple_settings import settings
from common_modules.parser import Parser


__author__ = 'Vadim Arsenev'
__version__ = '1.1.0'
__data__ = '30.08.2023'


def get_players():
    url = f'{settings.API_URL}/bootstrap-static/'
    requests_players = Parser(url)
    players = requests_players.parser_result()
    return players


def get_online_data(event_id):
    url = f'{settings.API_URL}/event/{event_id}/live/'
    requests_online = Parser(url)
    online_data = requests_online.parser_result()
    return online_data
