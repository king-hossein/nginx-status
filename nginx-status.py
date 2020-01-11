import requests
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://api.idogroup.ir/nginx_status'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

one_a_tag = soup.text

all = one_a_tag.split("requests")
numbers = all[1].split("Reading")
ahr = numbers[0].split(" ")

accepts = ahr[1]
handled = ahr[2]
requests = ahr[3]

print(accepts)
print(handled)
print(requests)

