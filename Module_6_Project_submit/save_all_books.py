"""def save_all_book(My_Library):
    with open("book_list.csv","w") as fb:
        for book in My_Library:
            line=f"{book["isbn"]},{book["title"]},{book["author"]},{book["p_year"]},{book["quantity"]}"
            fb.write(line)
"""


import json

def save_all_book(My_Library):
    with open("all_books.json", "w") as fp:
        json.dump(My_Library, fp, indent=4)