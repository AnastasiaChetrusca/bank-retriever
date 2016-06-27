from bs4 import BeautifulSoup
import urllib

def get_banks():

	page = urllib.urlopen('http://index.minfin.com.ua/bank/?mfo').read()
	soup = BeautifulSoup(page, 'html.parser')
	tables = soup.select("table ")
	Result = {}
	for table in tables:
		rows = table.select("tr")
		for row in rows:
			entries = row.select("td")
			if entries:
				Result[entries[0].text]=' BANK: '+entries[1].text + ' CITY: '+entries[2].text
	
	return Result



if __name__=="__main__":
	a = get_banks()
	type(a)
	for key in a:
		print key, a[key]

