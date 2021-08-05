"""State of internal structure."""


INTERNAL_STRUCTURE_FLAGS = {
    'unchanged': 'non_touched',
    'new': 'new',
    'old': 'old',
    'add': '+',
    'del': '-',
    'child': 'line'}

JSON_FLAGS = {
    'unchanged': 'not_toched',
    'new': 'new',
    'old': 'old',
    'add': 'added',
    'del': 'removed',
    'child': 'folded'}

STYLISH_FLAGS = {
    'unchanged': ' ',
    'new': '+',
    'old': '-',
    'add': '+',
    'del': '-',
    'child': ' '}
