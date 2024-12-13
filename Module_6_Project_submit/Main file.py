# Library Management System

import add_book
import book_view
import book_remove
import restore
import update
import lent
import returnbook

My_Library=[]


while True:
    print("Welcome to  My Library Manager App")
    print("======================")
    print("For Add Book Enter : 1")
    print("For  View Book List Enter : 2")
    print("For Remove/Delete Book from Library Enter : 3")
    print("For Edit/Update Book from Library Enter : 4")
    print("For Lent Book from Library Enter : 5")
    print("For Return Book to Library Enter : 6")
    print("For Exit From Library Manager App Enter : 7")
    print("======================")

    My_Library= restore.restore_all_books(My_Library)

    choice= input ("Enter Your Choice (1 to 7)  : ")

    if choice=="1":
        print("======================")
        My_Library= add_book.add_book(My_Library)
        print("======================")
    elif choice=="2":
        print("======================")
        book_view.view_all_book(My_Library)
        print("======================")
    elif choice=="3":
        print("======================")
        book_remove.remove_all_book(My_Library)
        print("======================")
    elif choice=="4":
        print("======================")
        update.update_book(My_Library)
        print("======================")
    elif choice=="5":
        print("======================")
        lent.lent_book(My_Library)
        print("======================")
    elif choice=="6":
        print("======================")
        returnbook.return_book(My_Library)
        print("======================")
    elif choice=="7":
        print("======================")
        print("Thanks for Using The App")
        print("======================")
        break
    else:
        print("Invalid Choice: Please Try Again")

# Kulsuma, Batch-3
