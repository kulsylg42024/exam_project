import datetime
import save_all_books


def return_book(My_Library):
    search_book = input("Enter Book Title to Return: ")
    for book in My_Library:
        if book["title"] == search_book:
           quantity = book["quantity"]+1
           book_return_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
           book["quantity"] = quantity
           book["bookLastUpdatedAt"] = book_return_at

           save_all_books.save_all_book(My_Library)
           print("Book Return Successfully")
           return My_Library

    print("Book Not Found")
