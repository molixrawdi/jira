import re
import cgitb
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

jira = JIRA ( options=server, basic_auth=(adminUser, adminPassword), validate=True )

BoardProjID = 'PSRV'

issue = "PSRV-1"  # raw_input("Enter a Jira ticket e.g. JEM-XXX")

subtask_one = {
    'project': {'key': 'PSRV-1'},
    'summary': 'Subtask name',
    'description': '',
    'issuetype': {'name': 'Sub-task'},
    'parent': {'id': issue},
    'assignee': {'name': 'user.name'},
}


subtask_two = {
    'project': {'key': 'PSRV-1'},
    'summary': 'Subtask name',
    'description': '',
    'issuetype': {'name': 'Sub-task'},
    'parent': {'id': issue},
    'assignee': {'name': 'user.name'},
}


subtask_three = {
    'project': {'key': 'PSRV-1'},
    'summary': 'Subtask name',
    'description': '',
    'issuetype': {'name': 'Sub-task'},
    'parent': {'id': issue},
    'assignee': {'name': 'user.name'},
}


if len ( issue ) > 0 and len ( issue ) <= 7:
    print ( "JEM issue validated" )
    subtasks = [subtask_one, subtask_two, subtask_three]
    for task in subtasks:
        child = jira.create_issue (fields=task)
    print ( "created child:{}".format ( str ( child.key ) ) )
elif len ( issue ) == 0:
    print ( "the input was empty" )
else:
    print ( "The following input was not valid" + issue )
