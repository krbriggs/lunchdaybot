from lxml import html
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
#from test_scraper import *


def convertHtml(html):
   html = html.replace('&nbsp;', ' ')
   html = html.replace('<p>', '')
   html = html.replace('</p>', '')
   html = html.replace('\t', '')
   html = html.replace('/b>', '')
   html = html.replace('-','')
   html = html.replace('<b>', '')
   html = html.replace('<br>', '')
   html = html.replace('<', '')
   return html

def getPickleDay(weekday):
   content = getContent()
   startIndex = content.find(weekday) + len(weekday) + 1
   food = content[startIndex:]
   
   endIndex = food.find('<')

   food = food[:endIndex]
   
   food = food.lstrip('<')
   #food = '\t' + food
   return convertHtml(food)

def getContent():
   #page = requests.get('http://dining.guckenheimer.com/clients/npcholdings/fss/fss.nsf/weeklyMenuLaunch/9W4S24~11-28-2016/%24file/cafehome.htm')
   page = requests.get('http://www.mrpickles.com/menu/soups')
   return page.content

def getPickleWeek():
   content = getContent()
   startIndex = content.find('Monday')

   endIndex = content.find('Friday') + content[content.find('Friday'):].find('<br')
   food = content[startIndex:endIndex]
   #print food
   foodweek = convertHtml(food).splitlines()
   food = ""
   for day in foodweek:
       food = food + "\t" + '- ' + day + "\n"
   return food[:-1]

def getMeal(day):
   content = getContent()

   food = getFoodDay(day, content)
   return food

def main():
   content = getContent()
   #print content
   
   food = getPickleDay('Monday')
   print food
   food = getPickleWeek()
   print food

if __name__ == "__main__":
   main()