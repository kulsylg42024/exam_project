# Project Name1 Contact Book Management System

print("hellow world")
import add_contract
import view_contract
import remove_contract
import update_contract

#l=load_contract.load_all_contract(phone_index)
phone_index = []


while True:
    print("Welcome to  My Cotract Book Management System")
    print("======================")
    print("For Add New Contract Enter : 1")
    print("For  View Contract List Enter : 2")
    print("For Remove Contract from Phone Index Enter : 3")
    print("For Exit From Cotract Book Management System Enter : 4")
    print("======================")

    choice= input ("Enter Your Choice (1 to 4)  : ")

    if choice=="1":
        print("======================")
        phone_index= add_contract.add_new_contract(phone_index)
        print("======================")
    elif choice=="2":
        print("======================")
        view_contract.view_all_contract(phone_index)
        print("======================")
    elif choice=="3":
        print("======================")
        phone_index=remove_contract.remove_all_contract(phone_index)
        print("======================")
    elif choice=="4":
        print("======================")
        print("Thanks for Using Cotract Book Management System Application")
        print("======================")
        break
    else:
        print("Invalid Choice: Please Try Again")
