
def num_validation(phone_index):
    if phone_index != []:
        phone_number = int(input("Enter phone number:"))
        for  contract in phone_index:
            if contract["pnum"] == phone_number:
               # phone_index.remove(contract)
               break       
               print("This Number Alrady Exist. Entry Fail")
    else:
        phone_number = int(input("Enter phone number:"))
    
        return phone_number