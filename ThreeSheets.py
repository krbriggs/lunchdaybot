import requests
import string
from bs4 import BeautifulSoup


def threeSheets():
    page = requests.get("http://www.threesheetscraftbeer.com/on-tap/")
    html = page.content
    html = html.replace('<strong>', ' * ')
    html = html.replace('</strong>', '* -')
    soup = BeautifulSoup(html)
    soup2 = soup.find("div", {"class": "row-fluid show-grid"})
    #soup2.replace('</strong>', '-')
    lines = soup2.get_text().splitlines()
    lines_real = ''
    '''
    print len(lines)
    print '\n'.strip()
    for line in lines:
        lines_real = lines_real + line
        if '-' not in line:
            lines_real += '\n'
    '''

    for i in range(len(lines)):
        try:
            if lines[i].strip() == '' and (lines[i+1] and lines[i+1].strip() == ''):
                i = i+1
            lines_real = lines_real + lines[i]
            if '*' not in lines[i]:
                lines_real += '\n'
        except:
            print ''

    #liness = [line.rstrip() for line in lines]
    return lines_real


def main():
   
   print threeSheets()
   

if __name__ == "__main__":
   main()