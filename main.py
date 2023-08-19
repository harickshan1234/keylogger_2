import os,time
print("✔ TO DO LIST MANAGER ✔😊")

my_list = []

def printlist():
    print()
    for item in my_list:
        print(item)
    print()

while True:
    user_input = str(input("DO you want to view,add, or remove or exit and from the to do list :  "))

    if user_input == "add":
        add = input("what are you going to add ? :  ")
        my_list.append(add)
    elif user_input == "remove":
        remove = str(input("which one are you going to remove : "))
        if remove in my_list:
            my_list.remove(remove)
        else:
            os.system("clear")
    elif user_input == "view":
        print(my_list)
    elif user_input == "exit":
        break
    
    else:
        print("invalid")
        break
    
printlist()       
        