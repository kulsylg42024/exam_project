import save_all_borrowers

def remove_borrower(Borrower_list):
    r= input("Enter the Borrower Name: ")

    for borrower in Borrower_list:
        if borrower["name"] == r:
            Borrower_list.remove(borrower)
            save_all_borrowers.save_all_borrower(Borrower_list)
            print("Borrower Removed/Deleted Successfully")
            return Borrower_list
    
    print("No Borrower in Borrower_List")