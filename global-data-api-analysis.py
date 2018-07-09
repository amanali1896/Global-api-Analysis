#install "requests" using pip install requests
#install "JSON" using pip install json
#this api displays the global data found at the top of coinmarketcap.com
import json #importing the libraries
import requests #importing the libraries
#giving the url link to a variable
global_url = 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(global_url) #this fethes the URL and returns the data in JSON format, assigning it to 'request' variable
