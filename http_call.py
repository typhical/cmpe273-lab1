#python3
#Tiffany Lee

import requests
import time

responseOne = requests.get('https://webhook.site/d74bc092-7e81-4429-bb06-148dc0c78c6e')
dateOne =  responseOne.headers['Date']
responseTwo = requests.get('https://webhook.site/d74bc092-7e81-4429-bb06-148dc0c78c6e')
dateTwo =  responseTwo.headers['Date']
responseThree = requests.get('https://webhook.site/d74bc092-7e81-4429-bb06-148dc0c78c6e')
dateThree =  responseThree.headers['Date']

print (dateOne)
print (dateTwo)
print (dateThree)
