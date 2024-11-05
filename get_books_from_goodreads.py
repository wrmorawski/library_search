import pandas as pd

def get_df_from_csv(path):
    # Get to-read entries from goodreads export csv
    books = pd.read_csv(path)
    return books[books['Bookshelves']=='to-read']

if __name__ == "__main__":
    print(get_df_from_csv('data/goodreads_library_export.csv'))

