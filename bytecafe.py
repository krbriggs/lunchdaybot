#from lxml import html
import requests
from ByteCafeUrl import byteCafeUrl

def getFoodDay(weekday, content):
   startIndex = content.find(weekday + ':')
   food = content[startIndex:]
   endIndex = food.find('<')

   food = food[:endIndex]
   food = food.lstrip('<')
   return food
   

def getContent():
   #page = requests.get('http://dining.guckenheimer.com/clients/npcholdings/fss/fss.nsf/weeklyMenuLaunch/9W4S24~11-28-2016/%24file/cafehome.htm')
   page = requests.get(byteCafeUrl())
   return page.content

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
