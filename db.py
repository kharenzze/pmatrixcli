import os
from tinydb import TinyDB, Query

HOME = os.path.expanduser("~")

FOLDER = f'{HOME}/.pmatrixcli'
PATH = f'{HOME}/.pmatrixcli/db.json'

if not os.path.exists(FOLDER):
  os.mkdir(FOLDER)

if not os.path.exists(PATH):
    with open(PATH, 'w+'): pass

db = TinyDB(PATH)