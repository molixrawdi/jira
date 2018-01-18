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

jira = JIRA(options=server, basic_auth=(adminUser, adminPassword), validate=True)


######GREEN HOPPER DEPRECATED FAIL########

# The code segment below failed to create sprint due to deprecated GreenHopper

# Sprint Creation syntax

# def create_sprint(self, name, board_id, startDate=None, endDate=None)

# Deprecated gh = GreenHopper

# self = "http://192.168.180.163:8080/jira/rest/kanban/1.0/sprint/"

# SprintName = 'SP Spring'

BoardProjID = 'PSRV'

# This above comes from Project ID check with relation to the project

# SprintStartDay = '18/Jan/18 10:10 AM'

# SprintEndDate = '22/Jan/18 17:50 PM'v7.7.0#77001-sha1:3be3151

# jira.create_sprint(SprintName, BoardProjID, SprintStartDay, SprintEndDate)

# create_sprint(SprintName,BoardProjID,SprintStartDay,SprintEndDate)BoardProjID

#issue_dict = {
#    'project': {'id': "BoardProjID "},
#    'summary': 'New issue from jira-python for work Servers Epic',
#    'description': 'Look into this Epic for Amy, this relate to servers',
#    'issuetype': {'name': 'Epic'},
#}

# new_issue = jira.create_issue(fields=issue_dict)


new_issue = jira.create_issue(project= BoardProjID, summary='New issue from Project Manager ',
                              description='Look into this one', issuetype={'name': 'Task'})