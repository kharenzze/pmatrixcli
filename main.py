import fire
from db import Data

class App(object):

  def save(self, token):
    Data.setToken(token)
    return 'Saved!'


  def read(self):
    token = Data.getToken()
    print(token)

if __name__ == '__main__':
  fire.Fire(App)