import fire
from db import db

class App(object):

  def save(self, text):
    db.insert({'text': text})
    return 'Saved!'


  def read(self):
    all = db.all()
    print(all)
    print('Read')

if __name__ == '__main__':
  fire.Fire(App)