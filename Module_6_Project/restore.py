import json

def restore_all_books(My_Library):
    with open("all_books.json", "r") as fp:
        My_Library = json.load(fp)
    return My_Library