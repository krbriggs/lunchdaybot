#from lxml import html
import requests
from ByteCafeUrl import byteCafeUrl

def convertHtml(html):
   html = html.replace('&nbsp;', ' ')
   html = html.replace('<p>', '')
   html = html.replace('</p>', '')
   html = html.replace('\t', '')
   return html

def getFoodDay(weekday, content):
   startIndex = content.find(weekday + ':') + len(weekday) + 1
   food = content[startIndex:]
   endIndex = food.find('<')

   food = food[:endIndex]
   food = food.lstrip('<')
   return convertHtml(food)

def getContent():
   #page = requests.get('http://dining.guckenheimer.com/clients/npcholdings/fss/fss.nsf/weeklyMenuLaunch/9W4S24~11-28-2016/%24file/cafehome.htm')
   page = requests.get(byteCafeUrl())
   return page.content

def getByteWeek():
   content = getContent()
   startIndex = content.find('Monday:')

   endIndex = content.find('Friday:') + content[content.find('Friday:'):].find('<')
   food = content[startIndex:endIndex]
   foodweek = convertHtml(food).splitlines()
   print foodweek
   food = ""
   for day in foodweek:
       food = food + "\t" + day + "\n"
   return food[:-1]

def getMeal(day):
   content = getContent()

   food = getFoodDay(day, content)
   return food

def main():
   content = getContent()
   food = getFoodDay('Monday', content)
   print food

if __name__ == "__main__":
   main()
