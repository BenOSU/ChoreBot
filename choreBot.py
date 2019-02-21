import requests
import time
from groupy import Client

request_params = {'token': '7bC53ZymUUULq74uIlnYHJ3WExGkGJMevOXGitY3'}
response_messages = requests.get('https://api.groupme.com/v3/groups/48409659/messages', params = request_params).json()['response']['messages']

response_users = requests.get('https://api.groupme.com/v3/groups/48409659/users', params = request_params).json()['response']['users']

print(response_users)

# client = Client.from_token('7bC53ZymUUULq74uIlnYHJ3WExGkGJMevOXGitY3')

to_send = '!!! Daily Whore Reminder !!! \n'

post_params = { 'bot_id' : '08a9497a271a70057028cd3b55', 'text': to_send }
requests.post('https://api.groupme.com/v3/bots/post', params = post_params)