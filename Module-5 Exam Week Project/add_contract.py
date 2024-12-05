from save_contract import save_all_contract
from num_validation import num_validation

def add_new_contract(phone_index):
    name1 =input("Enter the Person Name: ")
    phone_number= num_validation(phone_index)
    address=input("Enter the Person Address: ")
    email=input("Enter the Person Email Address:  ")
    
    contract= {
        "name": name1,
        "pnum": phone_number,
        "address": address,
        "email": email,
    }
    
    phone_index.append(contract)
        
    save_all_contract(phone_index)
    print ("Contract Save Successfully")

    
    return phone_index

