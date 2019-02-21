import requests
import time
import json

request_params = {'token': '7bC53ZymUUULq74uIlnYHJ3WExGkGJMevOXGitY3'}
response_messages = requests.get('https://api.groupme.com/v3/groups/48409659/messages', params = request_params).json()['response']['messages']

group = requests.get('https://api.groupme.com/v3/groups/48409659', params = request_params).json()['response']['members']

userIds = []

print(json.dumps(group, indent=4))

# client = Client.from_token('7bC53ZymUUULq74uIlnYHJ3WExGkGJMevOXGitY3')

to_send = '!!! Daily Whore Reminder !!! \n'

post_params = { 'bot_id' : '08a9497a271a70057028cd3b55', 'text': to_send }
requests.post('https://api.groupme.com/v3/bots/post', params = post_params)