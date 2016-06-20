from bs4 import BeautifulSoup
import urllib


def get_banks(index):
	r = urllib.urlopen('http://index.minfin.com.ua/bank/?mfo').read()
	soup = BeautifulSoup(r, 'html.parser')
	soup.select("table .bank")
	soup.select(".zebra tr")
	x=soup.select(".zebra tr")

	y=x[i]
	
	bankIDCode=y.select("td")[0].text
	dict={}
	dict['ID']=bankIDCode

	return dict


if __name__=="__main__":

	print "Existing banks"
	for i in range(1, 115):	
		print get_banks(i)

	print "Liquidated banks"				
	for i in range(116, 184):
		print get_banks(i)	

	print "Private banks"	
	for i in range(185, 232):
		print get_banks(i)	

