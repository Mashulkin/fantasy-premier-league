# -*- coding: utf-8 -*-
"""
Getting price players on gaffr
"""
import addpath
import sys
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

from functions.players import get_players, get_online_data
from functions.format import formatPosition, formatPrice, formatStatus
from functions.team import get_realTeam, get_onlineResults


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '30.08.2023'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS_ONLINE).split('\n')))


def realPlayers(players, online_data):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE_ONLINE[0], settings.COLUMNS_ONLINE, ORDER)
    for player in players['elements']:
        # ***** Main query *****
        if player['status'] == 'u':
            continue
        realPlayerId = player['code']
        firstName = player['first_name']
        lastName = player['second_name']
        webName = player['web_name']
        teamName, abbr = get_realTeam(players['teams'], player['team'])
        position = formatPosition(player['element_type'])
        seasonPlayerId = player['id']
        minutes, starts, goals, assists, clean_sheets, bonus, bps, points = \
            get_onlineResults(online_data['elements'], seasonPlayerId)

        # Gameweek data dictionary. Data generation and writing to file
        data_gameweek = {
            'firstName': firstName,
            'lastName': lastName,
            'webName': webName,
            'teamName': teamName,
            'abbr': abbr,
            'position': position,
            'minutes': minutes, 
            'starts': starts,
            'goals': goals,
            'assists': assists,
            'clean_sheets': clean_sheets,
            'bonus': bonus,
            'bps': bps,
            'points': points,
            'realPlayerId': realPlayerId,
            'seasonPlayerId': seasonPlayerId,
        }

        write_csv(settings.RESULT_FILE_ONLINE[0], \
            data_gameweek, ORDER)


def main():
    """
    Request information about the players. General request
    """
    actual_players = get_players()
    online_data = get_online_data(sys.argv[1])
    realPlayers(actual_players, online_data)


if __name__ == '__main__':
    remove_file(settings.RESULT_FILE_ONLINE[0])
    main()
