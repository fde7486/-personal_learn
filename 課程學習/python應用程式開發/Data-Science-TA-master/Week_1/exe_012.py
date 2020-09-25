import requests

url = 'http://www.fcu.edu.tw/1.html'
htmlfile = requests.get(url)
print (htmlfile.raise_for_status())