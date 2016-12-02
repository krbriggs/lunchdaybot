from bytecafe import *

def getSpecialtyContent():
   page = requests.get('https://www.specialtys.com/Location.aspx?Store=EB03#TodaysSoups')
   return page.content

def getSoups():
	content = getSpecialtyContent()
	startIndex = content.find('soupLinksContainer')
	content = content[startIndex:]
	endIndex = content.find('map streetView')
	content = content[:endIndex]

	lines = content.splitlines()
	soups = []

	for line in range(len(lines)):
		if 'index=' in lines[line]:
			soups.append(lines[line+1])

	return [convertHtml(soup.strip()) for soup in soups]

def main():
   content = getSoups()
   print content

if __name__ == "__main__":
   main()
