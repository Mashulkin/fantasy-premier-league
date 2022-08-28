# -*- coding: utf-8 -*-
"""
Getting player information from the FPL database
"""
from simple_settings import settings
from common_modules.parser import Parser


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '02.08.2021'


def get_players():
    url = f'{settings.API_URL}/bootstrap-static/'
    requests_players = Parser(url)
    players = requests_players.parser_result()
    return players
