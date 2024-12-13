
import json

def view_all_book(My_Library):
    with open("all_books.json", "r") as fp:
        My_Library = json.load(fp)

    if My_Library != []:
        for book in My_Library:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['p_year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}")
    else:
        print("No Book Found in My Library")