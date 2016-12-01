import os
import time
from slackclient import SlackClient

BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + str(BOT_ID) + ">"
EXAMPLE_COMMAND = "whats for lunch"

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
   #recieves commands directed at bot and determine if valid
   response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
      "* command with numbers, delimited by spaces."

   if command.startswith(EXAMPLE_COMMAND):
         response = "Sure... Bend Over"

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
