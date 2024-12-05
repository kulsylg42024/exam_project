from save_contract import save_all_contract

def remove_all_contract(phone_index):
    if phone_index != [] :
        phone_number= int(input("Enter the phone number what you want to remove: "))
        for contract in phone_index:
            if contract["pnum"] == phone_number: 
               phone_index.remove(contract)
               break
               
        print ("Contract remove Successfully")
    
    return phone_index        


