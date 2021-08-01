"""State of internal structure."""


STATES = {
    'unchanged': 'non_touched',
    'new': 'new',
    'old': 'old',
    'add': '+',
    'del': '-',
    'child': 'line',
    }

STATES_TO_JSON = {
    'unchanged': 'not_toched',
    'new': 'new',
    'old': 'old',
    'add': 'added',
    'del': 'removed',
    'child': 'folded',
    }

STATES_TO_STYLISH = {
    'unchanged': ' ',
    'new': '+',
    'old': '-',
    'add': '+',
    'del': '-',
    'child': ' ',
    }
