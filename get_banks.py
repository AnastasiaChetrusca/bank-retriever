from bs4 import BeautifulSoup
import urllib

def get_banks(index):

	page = urllib.urlopen('http://index.minfin.com.ua/bank/?mfo').read()
	soup = BeautifulSoup(page, 'html.parser')

	tables = soup.select("table")[index]
	result = {}
	rows = tables.select("tr")

	for row in rows:
		entries = row.select("td")

		if entries:

			key = entries[0].text
			bank = entries[1].text
			city = entries[2].text

			result[key]=(bank, city)
	
	return result


 
if __name__=="__main__":

	for i in range (0,3):

		if i == 0:
			print "\n\n\nExisting banks :"
		if i == 1:
			print "\n\n\nLiquidated banks :"
		if i == 2:
			print "\n\n\nPrivate banks :"		

		a = get_banks(i)
		for key, value in a.items():
			print key ,value[0], value[1]

