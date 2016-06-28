from bs4 import BeautifulSoup
import urllib

def get_banks():

	page = urllib.urlopen('http://index.minfin.com.ua/bank/?mfo').read()
	soup = BeautifulSoup(page, 'html.parser')
	tables = soup.select("table ")
	result = {}
	for table in tables:
		rows = table.select("tr")
		for row in rows:
			entries = row.select("td")
			if entries:
				result[entries[0].text] = ' BANK and City: '+ entries[1].text  #=' BANK: '+entries[1].text + ' CITY: '+entries[2].text
	
	return result


 
if __name__=="__main__":
	a = get_banks()
	type(a)
	for key in a:
		print key, a[key]

