import requests
from IPython.core.display import display, HTML

url = "http://pythonscraping.com/pages/cookies/welcome.php"
params = {"username":"fcu", "password":"password"}# post資料
html = requests.post(url, data=params)
print("Cookie:{}".format(html.cookies.get_dict()))