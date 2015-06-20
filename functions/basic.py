# functions.basic
# Implement ways to use the requests module for POST/GET requests
# Although requests works out of the box, this module should 
# oversimplify things.

import requests
import functions.strings

# some constants
UVA_HOME_PAGE = 'https://uva.onlinejudge.org'
UVA_LOGIN_PAGE = 'https://uva.onlinejudge.org/index.php?option=com_comprofiler&amp;task=login'
UVA_USERNAME_FIELD = 'username'
UVA_PASSWORD_FIELD = 'passwd'

class UVA:

  # Start a UVA Session using the specified username and password.
  def __init__(self, username='', passwd=''):
    self.s = requests.Session()
    self.payload = {}
    self.login(username, passwd)
    
  # Log in to a UVA Session.
  def login(self, username, passwd):
    self.payload[UVA_USERNAME_FIELD] = username
    self.payload[UVA_PASSWORD_FIELD] = passwd
    self.populate_payload()
    if raw_input("Proceed? ") != 'yes': return
    print self.s.post(UVA_LOGIN_PAGE, data=self.payload).text
    if self.check(): print "Cool! Logged in."
    else: print "Not logged in."
  
  # Check if already logged in or not.
  def check(self):
    if self.s.get(UVA_HOME_PAGE).text.find('Logout') == -1: return False
    else: return True       

  # populate form values using GET
  # (TODO) Probably use regular expressions.
  def populate_payload(self):
    resp = self.s.get(UVA_HOME_PAGE).text.split()
    foundName = False
    inForm = False
    nameStuff=None
    for resp_part in resp:
      if not inForm and resp_part == 'action="'+UVA_LOGIN_PAGE+'"': 
        inForm = True
      elif inForm:
        if resp_part[:5] == 'name=':
          foundName = True
          nameStuff = resp_part[6:-1]
        elif foundName and resp_part[:6] == 'value=':
          foundName = False
          self.payload[str(nameStuff)] = str(resp_part[7:-1])
        elif resp_part[-7:] == '</form>':
          inForm = False
    
