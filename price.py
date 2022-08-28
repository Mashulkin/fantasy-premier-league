# -*- coding: utf-8 -*-
"""
Getting price players on gaffr
"""
import addpath
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

from functions.players import get_players
from functions.format import formatPosition, formatPrice, formatStatus
from functions.team import get_realTeam


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '02.08.2021'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS).split('\n')))


def realPlayers(players):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE[0], settings.COLUMNS, ORDER)
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
        lineup = formatStatus(player['status'])
        gwPrice = formatPrice(player['now_cost'])
        bonus = '' # fake
        form = player['form']
        currentGW = '' # fake

        # Gameweek data dictionary. Data generation and writing to file
        data_gameweek = {
            'firstName': firstName,
            'lastName': lastName,
            'webName': webName,
            'teamName': teamName,
            'abbr': abbr,
            'position': position,
            'lineup': lineup,
            'gwPrice': gwPrice,
            'bonus': bonus,
            'realPlayerId': realPlayerId,
            'form': form,
            'currentGW': currentGW,
        }

        write_csv(settings.RESULT_FILE[0], \
            data_gameweek, ORDER)


def main():
    """
    Request information about the players. General request
    """
    actual_players = get_players()
    realPlayers(actual_players)


if __name__ == '__main__':
    remove_file(settings.RESULT_FILE[0])
    main()
