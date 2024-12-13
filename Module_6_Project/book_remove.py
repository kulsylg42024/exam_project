import save_all_books
import json

def remove_all_book(My_Library):
    r= input("Enter the book Title what you want to remove/delete: ")
    for book in My_Library:
        if book["title"] == r:
            My_Library.remove(book)
            save_all_books.save_all_book(My_Library)
            print("Book Removed/Deleted Successfully")
            return My_Library
    
    print("No Book Found for Remove/Delete such title name in My Library")


"""import save_all_books

def delete_books(all_books):
    search_book = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print("Book Deleted Successfully")
            return all_books
    
    print("Book Not Found")
"""