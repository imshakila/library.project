from datetime import date
def add() :
    national_code = input("enter your national code:")
    if national_code not in user_dic.keys() :
        names = input("enter your name:")
        last_names = input("enter your last name:")
        address = input("enter your address:")
        membership = "a" + national_code
        dates = date.today()
        user = {"names" :names,
                "last_names": last_names,
                "address": address,
                "membership": membership,
                "dates": dates
        }
        user_dic[national_code] = user
    else :
        print("exit!")    

def display() :
    for key, value in user_dic.items():
        print(key)
        for i, j in value.items():
            print(f"{i}--->{j}")

def edit(x) :
    for i in x :
        if i in user_dic.keys():
            national_code = input("enter your  new national code:")
            names = input("enter your new name:")
            last_names = input("enter your new last name:")
            address = input("enter your new address:")
            user_dic["national_code"]= national_code or user_dic["national_code"]
            user_dic["names"] = names or user_dic["names"]
            user_dic["last_names"] = last_names or user_dic["last_names"]
            user_dic["address"] = address or user_dic["address"]
            print("edited")
        else :
            print("not found") 

def remove(y):
    for i in y :
        if i in user_dic.keys():
            user_dic.pop(i)
            print("done")
        else:
            print("not found")  

#BOOK------------------------------------
def add():
    p_id =input("enter your p_id:")
    if p_id not in books_dic.keys():
        names_books = input("enter your name of book:")
        names_author = input("enter name of author:")
        year = int(input("enter the year of diffusion :"))
        field = input("enter field of book:")
        book = {"names_books":names_books,
                "names_author":names_author,
                "year":year,
                "field": field

        }
        books_dic[p_id]=book
    else:
        print("exit!")  
def display():
    for key, value in books_dic.items():
        print(key)
        for i, j in value.items():
            print(f"{i}--->{j}")

def edit(x):
    for i in x:
        if i in books_dic.keys():
            names_books = input("enter your name of book:")
            names_author = input("enter name of author:")
            year = int(input("enter the year of diffusion :"))
            field = input("enter field of book:")
        
            books_dic["names_books"] = names_books or books_dic["names_books"]
            books_dic["names_author"] = names_author or books_dic["names_author"]
            books_dic["year"] = year or books_dic["year"]
            print("edited")
        else :
            print("not found") 
def remove(y):
    for i in y:
        if i in books_dic.keys():
            books_dic.pop(i) 
            print("done")   
        else:
            print("not found")  
#def search(code):
    #for key, value in books_dic.items():
       # for code in books_dic.values():
            #if code==code:

           
            #print(value)


            
#USER--------------------------------------------------

choice = input("books or users:")
if choice == "users":
    user_dic = {}
    while True:
        user = input("add/remove/edit/display/exit:")
        if user == "add" :
            add()
       
        elif user == "remove":
            display()
            y = input("enter your national code to remove:")
            y = y.split()
            remove(y)

        elif user == "edit" :
            display()
            x = input("enter your natinal code")
            x = x.split()
            edit(x)

        elif user == "display":
            display()
        elif user == "exit" :
            break
        elif user == "" :
            pass
        else:
            print("command not found")

#BOOK-----------------------------------------------

elif choice == "books":
    books_dic = {}
    while True:
        user= input("add/remove/edit/display/exit/search:")
        if user == "add" :
            add()
       # print(user_dic)
        elif user == "remove":
            display()
            y = input("enter your national code to remove:")
            y = y.split()
            remove(y)

        elif user == "edit" :
            display()
            x = input("enter your natinal code")
            x = x.split()
            edit(x)

        elif user == "display":
            display()
        elif user == "search":
            pass
            #code = input("name or field :")  
            #search(code) 
        elif user == "exit" :
            break
        elif user == "" :
            pass
        else:
            print("command not found")









