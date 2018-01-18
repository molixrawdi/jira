import re

from collections import Counter

from jira import JIRA

# *************  GreenHopper HAS BEEN DEPRECATED ••••••••••••••••••••••••••••••

# Below is the code for simple connection authentication, Ideally we have a dedicated user

server = {'server': 'http://192.168.180.163:8080', 'verify': False, 'stream': True}

# Standard User

# user = 'user01'

# password = 'user01'

# Admin user

adminUser = 'admin'

adminPassword = 'admin'


print('starting script')

# options = {'server' : 'http://<server>.atlassian.net'}
jira = JIRA(options=server, basic_auth=(adminUser, adminPassword),validate=True)
jira.add_user('user01', 'user01@domain01.com', 'user01', 'User01', False, True, False)
# Above the 2nd 'user01' is actually a password, the third is an identifier

print('ending script')
