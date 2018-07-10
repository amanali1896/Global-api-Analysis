#install "requests" using pip install requests
#install "JSON" using pip install json
#this api displays the global data found at the top of coinmarketcap.com
import json #importing the libraries
import requests #importing the libraries
from datetime import datetime #importing this so that we can have a proper time format
#giving the url link to a variable
global_url = 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(global_url) #this fethes the URL and returns the data in JSON format, assigning it to 'request' variable
results = request.json() #converts the variable to a json format, and that is how we expect the results to be shown.
print(json.dumps(results, sort_keys=True, indent = 4))
#.dumps converts the result to a string. sort_keys is made true so that the keys are coming in a sorted order
#indent is made equal to 4 spaces because it prints it in an indented format
active_currencies = results['data']['active_cryptocurrencies']
#accessing the value of  results, we first go to the "Data"&then to its respective field in json
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quotes']['USD']['total_market_cap'])#going level by level as per the requirement
global_volume = int(results['data']['quotes']['USD']['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)#takes currencies and converts it into string separated by commas
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')#strftime means string from time https://linux.die.net/man/3/strftime

print()
print('There are currently ' + active_currencies_string + ' active cryptocurrecies and ' + active_markets_string + ' active markets.')
print('The global cap of all cryptos is ' + global_cap_string + ' and the 24h global volume is ' + global_volume_string + '.')
print('Bitcoin\'s total percentage of the global cap is ' + str(bitcoin_percentage) + '%.')
print()
print('This information was last updated on ' + last_updated_string + '.')
