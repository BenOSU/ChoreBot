import requests
import time
import json
import numpy
from pprint import pprint

request_params = {'token': '7bC53ZymUUULq74uIlnYHJ3WExGkGJMevOXGitY3'}
response_messages = requests.get('https://api.groupme.com/v3/groups/48409659/messages', params = request_params).json()['response']['messages']

group = requests.get('https://api.groupme.com/v3/groups/48409659', params = request_params).json()['response']['members']

member_dict = {}

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
chores = ['Dishwasher', 'Clean Countertops', 'Clean Stovetop']

member = {'AM': 30437530, 'BJ': 30693108, 'BS': 32706950, 'SG': 30107026, 'WD': 31580930, 'DP': 31628754, 'TM': 28709877, 'JC': 19049601}

current_week = None
choreMapping = numpy.zeros((3,7), int)

def createWeekMapping():
    whole_week = current_week.read().split("\n")
    for i in range(len(whole_week)):
        whole_week[i] = whole_week[i].split()
        for j in range(len(whole_week[i])):
            choreMapping[i][j] = int(whole_week[i][j])


current_week = open('current_week.txt')
if (current_week != None):
    createWeekMapping()
    print(choreMapping)

choreMapping = numpy.zeros((3,7), int)



member_dict = {}


for member in group:
    member_dict[member['nickname']] = member['user_id']


userIds = []

#print(json.dumps(group, indent=4))

# client = Client.from_token('7bC53ZymUUULq74uIlnYHJ3WExGkGJMevOXGitY3')

to_send = '!!! Daily Whore Reminder !!! \n'

post_params = { 'bot_id' : '08a9497a271a70057028cd3b55', 'text': to_send }
#requests.post('https://api.groupme.com/v3/bots/post', params = post_params)