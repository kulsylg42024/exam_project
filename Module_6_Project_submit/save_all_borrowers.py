import csv

def save_all_borrower(Borrower_list):
    with open("all_borrowers.csv", "w") as fb:
        for borrower in Borrower_list :
            line=f"{borrower["name"]},{borrower["phone_number"]},{borrower["title"]}, {borrower["quantity"]}, {borrower[ "when_book_return"]}, {borrower["booklentAt"]},{borrower["bookLastUpdatedAt"]}"
            fb.write(line)

       