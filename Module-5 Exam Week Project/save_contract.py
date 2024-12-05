import csv

def save_all_contract(phone_index):

    with open("contract_list.csv","w", newline='') as fb:
        csvFileWriter = csv.writer(fb)
        for contract in phone_index:
            line= f"{contract["name"]},{contract["pnum"]},{contract["address"]},{contract["email"]}"
            csvFileWriter.writerow(line) 

"""
with open("employee.csv",mode="w",newline='') as csvFile:
csvFileWriter = csv.writer(csvFile)
csvFileWriter.writerow(data)
"""