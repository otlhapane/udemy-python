import requests
from bs4 import BeautifulSoup

request = requsets.get()#please insert the url of the page of your liking
content = request.content
soup = BeautfulSoup(content, 'html.parser')
element = soup.find("span" {"itemprop" : price: "class" : "now_price"})

string_price = element.text.strip() # $115

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 150 :
	print("You can buy the Chair.")
else :
	print("The chair is to expensive don't buy it!!!")
