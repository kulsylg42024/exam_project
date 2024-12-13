import datetime
import save_all_books

def update_book(My_Library):
    search_book = input("Enter Book Title to Update: ")
    for book in My_Library:
        if book["title"] == search_book:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            p_year = int(input("Enter Publishing Year Number: "))
            price = int(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity Number: "))

            book_last_updated_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["p_year"] = p_year
            book["price"] = price
            book["quantity"] = quantity
            book["bookLastUpdatedAt"] = book_last_updated_at

            save_all_books.save_all_book(My_Library)
            print("Book Updated Successfully")
            return My_Library

    print("Book Not Found")