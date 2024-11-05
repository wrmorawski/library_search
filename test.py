# handle redirections 

import requests
from bs4 import BeautifulSoup

url = "https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx=ti&q=Rzekomo%20fajna%20rzecz%2C%20kt%C3%B3rej%20nigdy%20wi%C4%99cej%20nie%20zrobi%C4%99.%20Eseje%20i%20rozwa%C5%BCania"
# url = "https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx=ti&q=Ferdydurke"


response = requests.get(url, allow_redirects=True)  # allow_redirects is True by default

# Check the final URL after redirection
final_url = response.url
print("Final URL:", final_url)

# Now use BeautifulSoup to parse the final page content
soup = BeautifulSoup(response.text, 'html.parser')

book_elements = soup.find_all("a", {"class": "title"})
if not book_elements:
    book_elements = soup.find_all("h1", {"class": "title"})

# locations = soup.find_all("span", {"class": "ItemBranch"})
# locations = [loc.text.strip() for loc in locations]
# print(locations)


locations = soup.find_all("td", {"class": "location"})
locations = [loc.find('span').text.strip() for loc in locations]
print(set(locations))

print("Wypożyczalnia nr 17" in locations)

# print([book.text.strip() for book in book_elements])