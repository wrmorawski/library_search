from get_books_from_goodreads import get_df_from_csv
from get_books_from_library import get_books_from_library

if __name__ == "__main__":
    path = 'data/goodreads_library_export.csv'
    books = get_df_from_csv(path)
    main_url = "https://katalog.bpwlochy.waw.pl/cgi-bin/koha/opac-search.pl?idx={}&q="

    found_books = 0
    all_books = len(books)

    #
    print('number of books to search: ', len(books))
    
    for title in books['Title']:
        #Okay so after it is found it is redirected 
        #             # Specific for Goodreads handling of ISBN
        # if len(isbn) > 3:

        #     clear_isbn = isbn.replace("=", "").replace('"', '')
        results = get_books_from_library(title, main_url.format('ti'), prefered_locations=["Wypożyczalnia nr 28"])
        if results: 
            print(title, "znaleziono taką lub podobną ksiązkę ksiąkę")
            print(results)
            print()
            books= books[books['Title'] != title]
            found_books += 1



    print('number of books to search: ', all_books)
    print('found books: ', found_books)
