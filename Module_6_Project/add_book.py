from save_all_books import save_all_book
import random
import datetime

def add_book(My_Library):
    isbn = random.randint(10000, 99999)
    title =input("Enter the book title: ")
    author=input("Enter the book author name: ")
    p_year=int(input("Enter the book Publish Year:  "))
    
    price = int(input("Enter Book Price: "))
    bookAddAt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    
    book= {
        "isbn": isbn,
        "title": title,
        "author": author,
        "p_year": p_year,
        "quantity": quantity,
        "price": price,
        "bookAddAt": bookAddAt,
        "bookLastUpdatedAt": ""
    }
   
    My_Library.append(book)
    save_all_book(My_Library)

    print ("Book Save Successfully")
    return My_Library
