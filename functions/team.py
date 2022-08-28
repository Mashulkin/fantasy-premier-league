# -*- coding: utf-8 -*-
"""
Getting team name and abbreviation by ID in database
"""

__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '02.08.2021'


def get_realTeam(teamsData, realTeamId):
    teamName, abbr = [''] * 2
    
    if teamsData is None:
        return teamName, abbr

    for team in teamsData:
        if team['id'] == realTeamId:
            teamName = team['name']
            try:
                abbr = team['short_name']
            except KeyError:
                abbr = abbr
            break

    return teamName, abbr
