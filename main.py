
import os,time

print("To Do List Manager:")
mylist = []

def printlist():
  print()
  for item in mylist:
    print(item)
  print()

while True:
  user_input = input("Do you want to view, add, edit, or remove or exit an item from the to do list? : ")
  if user_input == "view":
    print(mylist)
  elif user_input == "add":
    ad_list = input("What do you want to add : ")
    mylist.append(ad_list)
  elif user_input == "remove":
    re_list = input("What do you want to remove? : ")
    if re_list in mylist:
      kali = input("Are you sure you want to remove this? : ")
      if kali == "yes":
        mylist.remove(re_list)
      else:
        os.system("clear")
  elif user_input == "exit":
    break

  else:
    print("invalid")
    break

