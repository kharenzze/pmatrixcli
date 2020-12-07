import fire
from db import Data
from prioritymatrix import PM

def getPM():
  token = Data.getToken()
  if not token:
    raise 'You need to set a token'
  return PM("https://sync.appfluence.com/api/v1/", token)

class App(object):

  def token(self, token):
    Data.setToken(token)
    return 'Saved!'

  def show_token(self):
    token = Data.getToken()
    print(token)

if __name__ == '__main__':
  fire.Fire(App)