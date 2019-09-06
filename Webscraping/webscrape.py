from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#opening up connection, grabbing the page
my_url = 'https://www.royallepage.ca/en/on/waterloo/properties/' 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

#grabs each real estate listed
containers = page_soup.findAll('div', {'class': 'card card--listing-card js-listing js-property-details'})

#opens a csv file
filename = "waterlooHousing_page1.csv"
f = open(filename, 'w')
headers = 'address, house type, # of beds, # of baths, price\n'
f.write(headers)

#loops through all containers on the page
for container in containers:

	#grabs type of real estate
	type_container = container.findAll('div', {'class': 'listing-meta listing-meta--small'})
	if type_container[0].span.text != "Commercial" and type_container[0].span.text != "Investment" and type_container[0].span.text != "Vacant Land":
		housetype = type_container[0].span.text 

		#grabs address of real estate
		address_container = container.findAll('address', {'class': 'address-1'})
		address = address_container[0].a.text


		#grabs number of beds
		bed_container = container.findAll('div', {'class': 'listing-meta listing-meta--small'})
		bed = bed_container[0].select_one('div span:nth-of-type(2)').text[0]

		#grabs number of baths
		bath_container = container.findAll('div', {'class': 'listing-meta listing-meta--small'})
		bath = bath_container[0].select_one('div span:nth-of-type(2)').text[8]

		#grabs price of real estate
		price_container = container.findAll('h3', {'class': 'price'})
		price = price_container[0].span.text

		print('address: ' + address)	
		print('type: ' + housetype)
		print('bed: ' + bed)
		print('bath: ' + bath)
		print('price: ' + price)

		#writes brand, name, and shipping price of product to the csv file
		f.write(address + "," + housetype + "," + bed + "," + bath + "," + price.replace(',' , ' ') + "\n")

f.close()