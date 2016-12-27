import os
import time
from slackclient import SlackClient
import random

BOT_ID = os.environ["BOT_ID"]

AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

sc = SlackClient(os.environ['SLACK_BOT_TOKEN'])

def generate(text):
	input_text = text.split("do")[1].strip().lower()
	
	tokens = input_text.split()
	list = random.sample(range(len(tokens)),len(tokens))

	s_list = []
	for num in list:
		s_list.append(tokens[num])

	out_string = ' '.join(s_list)
	return out_string

def parse(read_list):
	
	if read_list and len(read_list) > 0: # Something is actually read from slack 
		for read in read_list:
			if read and 'text' in read and AT_BOT in read['text']:
				
				return read['text'].split(AT_BOT)[1].strip().lower(),read['channel']
				
	return None,None

def handle_command(command,channel):
	
	response = "Did not get you, try "

	if command.startswith(EXAMPLE_COMMAND):
		response = generate(command)

	sc.api_call("chat.postMessage",channel=channel,text=response, as_user=True)

if __name__ == '__main__':
	if sc.rtm_connect():
		while True:
			print("Connected and Running")
			command, channel = parse(sc.rtm_read())

			if command and channel:
				handle_command(command,channel)

			time.sleep(1)
	else:
   	    print("Connection Failed, invalid token?")	





