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

class Data(object):
  table = db.table('session')

  @classmethod
  def getToken(cls):
    try: 
      data = cls.table.all()[0]
      return data['token']
    except:
      return None

  @classmethod
  def setToken(cls, token):
    cls.table.truncate()
    cls.table.insert({ "token": token })