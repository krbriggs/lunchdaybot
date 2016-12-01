from lxml import html
import requests


def getFoodDay(weekday, content):
   startIndex = content.find(weekday + ':')
   food = content[startIndex:]
   endIndex = food.find('<')

   food = food[:endIndex]
   food = food.lstrip('<')
   return food
   

def getUrl():
   page = requests.get('http://dining.guckenheimer.com/clients/npcholdings/fss/fss.nsf/weeklyMenuLaunch/9W4S24~11-28-2016/%24file/cafehome.htm')
   return page.content


def main():
   content = getUrl()
   food = getFoodDay('Monday', content)
   print food

if __name__ == "__main__":
   main()
