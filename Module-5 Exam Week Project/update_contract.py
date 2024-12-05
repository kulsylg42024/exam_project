"""
from view_contract import view_all_contract

def update_all_contract(phone_index):
    with open("contract_list.csv","r") as fb:
        for contract in phone_index:
            line=f"{contract["name"]},{contract["pnum"]},{contract["address"]},{contract["email"]}"
            fb.read(line)
            
            phone_index.update(contract)
            view_all_contract(phone_index)
            
    return (phone_index)
    """