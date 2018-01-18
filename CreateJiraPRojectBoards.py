import re

from collections import Counter

from jira import JIRA

from jira.client import GreenHopper

# Below is the code for simple connection authentication, Ideally we have a dedicated user

server = {'server': 'http://192.168.180.163:8080', 'verify': False, 'stream': True}

# Standard User

# user = 'user01'

# password = 'user01'

# Admin user

adminUser = 'admin'

adminPassword = 'admin'

jira = JIRA(options=server, basic_auth=(adminUser, adminPassword), validate=True)

# Basic tasks:


# Step 01 Create a new Project: infra

# Step 02 Create a new Board

# Step 03 Create a new Sprint(s)


# Syntax template is below, will use this to start with


# create_project(self, key, name=None, assignee=None, type="Software", template_name=None)

ProjKey = "PSRV" # this field is a very short string

ProjName = "PrjSRV"

ProjAssignee = "admin"

ProjType = "Software"

ProjTemplateName = "Jira Classic"

jira.create_project(ProjKey, ProjName, ProjAssignee, ProjType, ProjTemplateName)

# variable above key is mandatory and has to match JIRA project key requirements, usually only 2-10 uppercase characters

# If Project name wasn't found then the key will be used instead


# Create the board relating to the project

# Board creation syntax

# create_board(self, name, project_ids, preset="scrum")


BoardName = "Brd1"

BoardProjID = "PSRV" # Max string size is 4 letters only in capital MUST REMEMBER

# BoardProjPreset = "scrum" # the team decided on kanban

BoardProjPreset = "kanban"

jira.create_board(BoardName, BoardProjID, BoardProjPreset)

