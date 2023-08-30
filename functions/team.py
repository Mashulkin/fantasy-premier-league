# -*- coding: utf-8 -*-
"""
Getting team name and abbreviation by ID in database
"""

__author__ = 'Vadim Arsenev'
__version__ = '1.1.0'
__data__ = '30.08.2023'


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


def get_onlineResults(data, seasonPlayerId):
    minutes, starts, goals, assists, clean_sheets, bonus, bps, points = [''] * 8
    for item in data:
        if seasonPlayerId == item['id']:
            minutes = item['stats']['minutes']
            starts = item['stats']['starts']
            goals = item['stats']['goals_scored']
            assists = item['stats']['assists']
            clean_sheets = item['stats']['clean_sheets']
            bonus = item['stats']['bonus']
            bps = item['stats']['bps']
            points = item['stats']['total_points']
            break
    
    return minutes, starts, goals, assists, clean_sheets, bonus, bps, points
