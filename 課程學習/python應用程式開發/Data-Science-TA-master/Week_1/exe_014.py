
import requests
from bs4 import BeautifulSoup

package = {'firstname': 'Rich', 'lastname': 'Wu'} # 傳送資料

html = requests.post("http://pythonscraping.com/pages/processing.php", data=package)
print(html.text)