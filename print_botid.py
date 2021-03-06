import os
from slackclient import SlackClient

BOT_NAME = "YOUR_BOT_NAME"

slack_token = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

if __name__ == '__main__':

	user_list = sc.api_call("users.list")
	if user_list['ok']: # If request gets executed properly 
 
		users = user_list['members'] # Get list of all users

		for user in users:
			if user['name'] == BOT_NAME:
				print("BOT ID " + ": " + user['id'])
	else:

		print("Could not get bot id")
