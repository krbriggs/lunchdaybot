from lxml import html
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
import random




def lunch():
  lunch_options = ['chipotle', 'chipotle', 'specialtys', 'workday snack program', 'in n out', 'chick fil a', 'mcdonalds', 'fat fish', 'poke don', 'byte cafe', 'new york pizza', 'food truck', 'urban plates', 'panda express', 'cpk', 'cheesecake factory', 'mr. pickles', 'taco bell', 'buckhorn grill', 'chipotle', 'hisui express', 'sendo sushi', 'IKEA', 'chuck e cheese', 'little sheep', 'dim sum', 'pho', 'thai', 'chipotle', 'local poke', 'khyber pass', '']
  lunch_choice = (random.choice(lunch_options))
  #print lunch_choice
  return lunch_choice


def main():
   lunch()
   #cheesy()
   return 'cheesy'
   

if __name__ == "__main__":
   main()