print("exam")

import f_terms

my_num = ()

while True:
    print("Welcome to  My F_Number App")
    print("======================")
    print("For Generate the Fibonacci series up to a specific number of terms Enter : 1")
    print("For Generate the Fibonacci series up to a specific number of maximum value : 2")
    print("For Exit Enter : 3") 
    print("======================")

    choice= input ("Enter Your Choice (1 to 3)  : ")

    if choice=="1":
        print("======================")
        f_terms.f_want_term(my_num )
        print("======================")
    elif choice=="2":
        
        print("======================")
    elif choice=="3":
        print("======================")
        print("Thanks for Using The App")
        print("======================")
        break
    else:
        print("Invalid Choice: Please Try Again")
