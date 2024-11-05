import requests
from bs4 import BeautifulSoup
import random
from urllib.parse import quote

def get_books_from_library(text, url, location = None):
    # Format the city for use in the URL
    text = quote(text)

    # Create the URL (assumption: the search text is at the end)
    url = url+text

    # Set headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code != 200:
        print("Failed to retrieve data from your library.")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find books names
    book_elements = soup.find_all("a", {"class": "title"})
    if not book_elements:
        book_elements = soup.find_all("h1", {"class": "title"})

    if location: 
        all_locations = soup.find_all("span", {"class": "ItemBranch"})
        all_locations = [loc.text.strip() for loc in all_locations]
        if all_locations: 
            print(set(all_locations))
            if location in all_locations: 
                print("ksiąka znajduje się w wypozyczalni")
            else: 
                print("ksiązka jest w innej lokalizacji")  
        else:
            all_locations = soup.find_all("td", {"class": "location"})
            all_locations = [loc.find("span").text.strip() for loc in all_locations]
            if all_locations:
                print(set(all_locations))   
                if location in all_locations: 
                    print("ksiąka znajduje się w wypozyczalni")
                else: 
                    print("ksiązka jest w innej lokalizacji")
    
    books = [book.text.strip() for book in book_elements]
    
    if not books:
        # print("No books found. Please check the city name or try again.")
        return None
        # return url
    else:
        return url

def get_books_from_library_by_author(author):
    pass

if __name__ == "__main__":
    # Example usage
    # title = 'Harry Potter'
    title = "Słownik ortograficzny"
    books = get_books_from_library(title, 'https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx=ti&q=')
    print(books)
    print("the end")



# https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx=nb&q=9780300082401 ISBN URL
# https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx=&q=ferdydurke General URL
# https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx=au&q=Pielewin Author URL
# https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx=ti&q=%C5%BBycie Title URL ?? DOES IT WORK FOR ENGLISH TITLES AS WELL? #trzeba zmienić kodowanie polskich znaków