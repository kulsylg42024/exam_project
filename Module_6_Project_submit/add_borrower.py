import datetime
import save_all_borrowers

Borrower_list=[]

def add_brrower(Borrower_list):
    name= input("Enter your Name: ")
    phone_number=int(input("Enter Your Phone Number: "))
    title =input("Enter the book title: ")
    quantity=1
    when_book_return= ("Enter Book Return Date: ")
    booklentAt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    
    
    borrower= {
        "name": name,
        "phone_number": phone_number,
        "title": title,
        "quantity": quantity,
        "when_book_return": when_book_return,
        "booklentAt": booklentAt,
        "bookLastUpdatedAt": ""
    }
   
    Borrower_list.append(borrower)
    save_all_borrowers.save_all_borrower(Borrower_list)

    print ("Borrower Save Successfully")
    return Borrower_list

