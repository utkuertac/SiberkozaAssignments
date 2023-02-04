# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules

# import
import datetime

today_ue = datetime.date.today()

print(today_ue)

# from
import datetime
from datetime import date

today_ue = date.today()

print(today_ue)

#
import datetime
from datetime import date
import time

today = date.today()
timestamp_ue = time.time()

print(timestamp_ue)

#
import datetime
from datetime import date
import time
from time import time

today = date.today()
timestamp_ue = time()

print(timestamp_ue)

# Pip module

# pip (pip3 install camelcase)(global)

from camelcase import CamelCase

c_ue = CamelCase()
print(c_ue.hump('hello there world'))

# Import custom modul
import validator_ue
from validator_ue import validate_email

email_ue = 'test@test.com'
if validate_email(email_ue):
  print('Email is valid')
else:
  print('Email is bad')
  
