from bots.botsconfig import *
from .records005040 import recorddefs

syntax = {
    'version': '00504',
    'functionalgroup': 'SO',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'X01', MIN: 1, MAX: 1},
        {ID: 'X02', MIN: 0, MAX: 9999},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
