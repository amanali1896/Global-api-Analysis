#install "requests" using pip install requests
#install "JSON" using pip install json
#this api displays the global data found at the top of coinmarketcap.com
import json #importing the libraries
import requests #importing the libraries
#giving the url link to a variable
global_url = 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(global_url) #this fethes the URL and returns the data in JSON format, assigning it to 'request' variable
results = request.json() #converts the variable to a json format, and that is how we expect the results to be shown.
print(json.dumps(results, sort_keys=True, indent = 4))
#.dumps converts the result to a string. sort_keys is made true so that the keys are coming in a sorted order
#indent is made equal to 4 spaces because it prints it in an indented format
