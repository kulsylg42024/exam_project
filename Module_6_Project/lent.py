import datetime
import save_all_books


def lent_book(My_Library):
    search_book = input("Enter Book Title to Lent: ")
    for book in My_Library:
        if book["title"] == search_book:
           if book["quantity"] !=0:
              quantity = book["quantity"]-1
              book_lent_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
              book["quantity"] = quantity
              book["bookLastUpdatedAt"] = book_lent_at

              save_all_books.save_all_book(My_Library)
              print("Book Lent Successfully")
              return My_Library

    print("Book Not Found")
