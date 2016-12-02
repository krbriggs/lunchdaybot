import os
import time
import datetime
from slackclient import SlackClient
from bytecafe import *
from specialtys import getSoups
from FoodTruckMafia import foodTruckMafia
from mrpickles import getPickleDay
from mrpickles import getPickleWeek

BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + str(BOT_ID) + ">"
EXAMPLE_COMMAND1 = "today"
EXAMPLE_COMMAND2 = "week"
EXAMPLE_COMMAND3 = "cheesecake"
EXAMPLE_COMMAND4 = "pickle soup"
EXAMPLE_COMMAND5 = "IKEA"

week = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def getCurrentDay():
   date = datetime.date.today()
   day = date.weekday()
   return week[day]

def handle_command(command, channel):
   #recieves commands directed at bot and determine if valid
   response = "Not sure what you mean. These are the supported commands:\n"
   response += '\t' + EXAMPLE_COMMAND1 + '\n \t' + EXAMPLE_COMMAND2 + '\n \t' + EXAMPLE_COMMAND3 + '\n \t' + EXAMPLE_COMMAND4 + '\n'

   if command.startswith(EXAMPLE_COMMAND1):
         response = '*Byte Cafe:*\n\t' + getMeal(getCurrentDay())
         response += '\n*Specialty\'s Soups:*'
         soups = getSoups()
         for soup in soups:
            response += '\n\t' + soup
         if getCurrentDay() == 'Friday':
            response += '\n*Food Truck Mafia:*\n' + foodTruckMafia()

   if command.startswith(EXAMPLE_COMMAND2):
         response = '*Byte Cafe:*\n' + getByteWeek()
         response += '\n*Food Truck Mafia:*\n' + foodTruckMafia()

   if command.startswith(EXAMPLE_COMMAND3):
         response = '*Cheesecake Factory Cheesecakes:*\n'
         response += cheese()

   if command.startswith(EXAMPLE_COMMAND4):
         response = '*Mr. Pickles Soups:*\n'
         response += "Today's Soup:\n "
         response += '\t' + '- ' + getPickleDay('Friday')
         response += "\nThis Week's Soups:\n"
         response += getPickleWeek()

   if command.startswith(EXAMPLE_COMMAND5):
         response = "Swedish Meatballs"

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
