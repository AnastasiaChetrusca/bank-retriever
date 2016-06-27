Bank page retriever for Ukraine
-------------------------------

Description
-----------

Bank page retriever function ``get_banks`` for ``http://index.minfin.com.ua/bank/?mfo`` that does the following:

	* Connects to that URL and retrieves its data
	* Processes the page contents and returns the ``Bank Identifier Codes``


Dependencies
============

- Python 2.7 or later (http://www.python.org/)

- Virtualenv: Virtualenv is a tool that creates an isolated Python environment for each of your projects. 

- Beautiful Soup: Beautiful Soup is a Python library for pulling data out of HTML and XML files.

- lxml 2.0 or later. Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers. One is the lxml parser.The easiest way to do so is to install ``lxml`` from (http://lxml.de/) or if you use git ``git clone git://github.com/lxml/lxml.git lxml`` .


Installing and activating Virtualenv
====================================

        pip install virtualenv
		virtualenv venv-bak
		source venv-bank/bin/activate
 


Making the soup
---------------

1. Create a new python file in virtual environment (venv-bak).

2. Let's start by importing in the new python file the ``BeautifulSoup`` from ``bs4`` and the ``urllib`` module :
		
		from bs4 import BeautifulSoup
		import urllib

3. Create the ``get_banks`` function:

		
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

4. Create the ``main`` function wich contains 3 loops for proccesing and retrieving the data for each table :	

		if __name__=="__main__":
			a = get_banks()
			type(a)
			for key in a:
				print key, a[key]	

References
----------

- https://hackercodex.com/guide/python-development-environment-on-mac-osx/
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup
- http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
- http://index.minfin.com.ua/bank/?mfo

