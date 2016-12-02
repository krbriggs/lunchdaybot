import os
import time
import datetime
from slackclient import SlackClient
from bytecafe import *
from specialtys import getSoups

BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + str(BOT_ID) + ">"
EXAMPLE_COMMAND1 = "today"
EXAMPLE_COMMAND2 = "week"

week = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def getCurrentDay():
   date = datetime.date.today()
   day = date.weekday()
   return week[day]

def handle_command(command, channel):
   #recieves commands directed at bot and determine if valid
   response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND1 + \
      "* command with numbers, delimited by spaces."

   if command.startswith(EXAMPLE_COMMAND1):
         response = 'Byte Cafe:\n\t' + getMeal(getCurrentDay())
         response += '\nSpecialty\'s Soups:'
         soups = getSoups()
         for soup in soups:
            response += '\n\t' + soup

   if command.startswith(EXAMPLE_COMMAND2):
         response = 'Byte Cafe:\n' + getByteWeek()

   slack_client.api_call("chat.postMessage", channel=channel, text=response,
      as_user=True)

def parse_slack_output(slack_rtm_output):
   #return None unless message is for bot
   output_list = slack_rtm_output
   
   if output_list and len(output_list) > 0:
      for output in output_list:
         if output and 'text' in output and AT_BOT in output['text']:
            #return text w/o whitespace
            return output['text'].split(AT_BOT)[1].strip().lower(), \
               output['channel']

   return None, None

if __name__ == "__main__":
   READ_WEBSOCKET_DELAY = 1

   if slack_client.rtm_connect():
      print("StarterBot connected and running")
      while True:
         command, channel = parse_slack_output(slack_client.rtm_read())
         
         if command and channel:
            handle_command(command, channel)
         time.sleep(READ_WEBSOCKET_DELAY)

   else:
      print("Connection failed. Invalid Slack token or bot ID")
