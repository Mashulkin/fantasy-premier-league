# -*- coding: utf-8 -*-
"""
Getting ownership players on gaffr
"""
import addpath
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

from functions.players import get_players
from functions.format import formatPosition, formatPrice
from functions.team import get_realTeam


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '02.08.2021'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS_OWN).split('\n')))


def realPlayers(players):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE_OWN[0], settings.COLUMNS_OWN, ORDER)
    for player in players['elements']:
        # ***** Main query *****
        if player['status'] == 'u':
            continue
        realPlayerId = player['code']
        lastName = player['second_name']
        webName = player['web_name']
        teamName, abbr = get_realTeam(players['teams'], player['team'])
        position = formatPosition(player['element_type'])
        seasonPrice = formatPrice(player['now_cost'])
        gwPrice = '' # fake
        gameweek = '' # fake
        selectedRatio = player['selected_by_percent']
        totalPoints = player['total_points']
        gwPoints = player['event_points']
        minutesPlayed = '' # fake
        captainedRatio = '' # fake
        fieldTeam = '' # fake
        abbrRival = '' # fake

        # Gameweek data dictionary. Data generation and writing to file
        data_gameweek = {
            'lastName': lastName,
            'webName': webName,
            'teamName': teamName,
            'abbr': abbr,
            'position': position,
            'seasonPrice': seasonPrice,
            'gwPrice': gwPrice,
            'realPlayerId': realPlayerId,
            'gameweek': gameweek,
            'selectedRatio': selectedRatio,
            'totalPoints': totalPoints,
            'gwPoints': gwPoints,
            'minutesPlayed': minutesPlayed,
            'captainedRatio': captainedRatio,
            'fieldTeam': fieldTeam,
            'abbrRival': abbrRival,
        }

        write_csv(settings.RESULT_FILE_OWN[0], \
            data_gameweek, ORDER)


def main():
    """
    Request information about the players. General request
    """
    actual_players = get_players()
    realPlayers(actual_players)


if __name__ == '__main__':
    remove_file(settings.RESULT_FILE_OWN[0])
    main()
