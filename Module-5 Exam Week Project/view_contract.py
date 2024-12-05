def view_all_contract(phone_index):
    
    if phone_index != []:
        for contract in phone_index:
            print(f" Name:{contract["name"]}, Phone Number:{contract["pnum"]}, Address:{contract["address"]}, Email:{contract["email"]}")
    else:
        print("No contract in phone index ")
    return phone_index





"""
with open("employee.csv",mode="w",newline='') as csvFile:
csvFileWriter = csv.writer(csvFile)
csvFileWriter.writerow(data)
"""