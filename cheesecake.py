from lxml import html
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib


def cheese():
  r = urllib.urlopen('https://www.thecheesecakefactory.com/menu/desserts/cheesecakes').read()
  soup = BeautifulSoup(r, "lxml")
  cakes = soup.find_all("span", class_="item-title")
  
  cakes_with_newlines = 'Original' + '\n'
  for element in cakes:
         title = element.get_text()
         if title.find('Cheesecake') > -1:
            cakes_with_newlines = cakes_with_newlines + title + '\n'
  return cakes_with_newlines


def main():
   content = getContent()
   #cheese(content)
   #cheesy()
   return 'cheesy'
   

if __name__ == "__main__":
   main()