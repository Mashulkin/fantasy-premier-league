# -*- coding: utf-8 -*-
"""
Real player position formatting on the FPL 
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '10.10.2020'


def formatPosition(positionId):
    position = ''
    position = 'GK' if positionId == 1 else position
    position = 'D' if positionId == 2 else position
    position = 'M' if positionId == 3 else position
    position = 'F' if positionId == 4 else position

    return position


def formatPrice(price):
    try:
        price = '{:.1f}'.format(float(price) / 10)
    except TypeError:
        price = ''
    except ValueError:
        price = ''
    
    return price


def formatStatus(status):
    status = 'injured' if status == 'i' else status
    
    return status
