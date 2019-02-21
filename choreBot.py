import requests
import time
import json
import numpy
import datetime
from pprint import pprint

todays_people = None

request_params = {'token': '7bC53ZymUUULq74uIlnYHJ3WExGkGJMevOXGitY3'}
response_messages = requests.get('https://api.groupme.com/v3/groups/48409659/messages', params = request_params).json()['response']['messages']

print(response_messages)

group = requests.get('https://api.groupme.com/v3/groups/48409659', params = request_params).json()['response']['members']

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
chores = ['Dishwasher', 'Clean Countertops', 'Clean Stovetop']

member_array = [30437530, 30693108, 32706950, 30107026, 31580930, 31628754, 28709877, 19049601]
member_dict = {30437530: 'AM', 30693108: 'BJ', 32706950: 'BS', 30107026: 'SG', 31580930: 'WD', 31628754: 'DP', 28709877: 'TM', 19049601: 'JC'}

current_week = None
choreMapping = numpy.zeros((3,7), int)

# reads the current Week from the JSON file
def createWeekMapping():
    whole_week = current_week.read().split("\n")
    for i in range(len(whole_week)):
        whole_week[i] = whole_week[i].split()
        for j in range(len(whole_week[i])):
            choreMapping[i][j] = int(whole_week[i][j])

# starts a new chore week by shifting everybody to the left
def shiftWeek():
    for i in range(choreMapping.shape[0]):
        for j in range(choreMapping.shape[1]):
            id = choreMapping[i][j]
            mem_index = member_array.index(id)
            if mem_index < 7:
                choreMapping[i][j] = member_array[mem_index + 1]
            else:
                choreMapping[i][j] = member_array[0]



current_week = open('current_week.txt')
if (current_week != None):
    createWeekMapping()
    print(choreMapping)
    print()
    shiftWeek()
    print(choreMapping)
    day_of_week = datetime.datetime.today().weekday() # get the current weekday
    todays_people = choreMapping[:,day_of_week]
    print(todays_people)


to_send = '@Alec Maier  Hey'

# TODO: correct this to use Loci. We will need to insert nicknames into the message text and use locis to map the mentions to them. 
# refer to the mentions section of the docs for groupy https://media.readthedocs.org/pdf/groupy/stable/groupy.pdf
mentions = "{'loci': [[0,11]], 'type': 'mentions', 'user_ids': ['30437530']}"

print(mentions)

post_params = { 'bot_id' : '08a9497a271a70057028cd3b55', 'text': to_send, 'attachments': [mentions] }
request = requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
print(request.content)