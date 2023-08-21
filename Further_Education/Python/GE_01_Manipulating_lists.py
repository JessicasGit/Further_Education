"""
15.02.2023
Manipulating lists
Created by: Jessica Göckler
"""
list1 = list(range(20))
list2 = list(range(3,20))
list3 = list(range(2,20,2))
# Asking for the type of specification
List_input1 = input("Choose between 1, 2 and 3 specifications for your list: \n"
                    "1 = One specification, \n"
                    "2 = Two specifications, \n"
                    "3 = Three specifications \n")
#  Asking what kind of manipulation should be done
List_input2 = input("Now you can manipulate your list. \n"
                     "+ = Define what you add where in your list \n"
                     "- = Removes an element of your choise from your list \n"
                     "4 = Reverses the order of the list \n"
                     "5 = Is returning the entry of the list \n"
                     "6 = Searching for something you want \n")
# Manipulate list1
if List_input1 == "1":
    print(list1)
# Adding
    if List_input2 == "+":
        list1.insert(int(input()),int(input()))
        print(list1)
# removing
elif List_input2 == "-":
        list1.remove(int(input()))
        print(list1)
# put list in reverse
elif List_input2 == "4":
        list1.reverse()
        print(list1)
# Returning the entry
elif List_input2 == "5":
        print(list1.index(1))
# searching for something
elif List_input2 == "6":
        check1 = int(input("Which number are you looking for? "))
        if check1 in list1:
               print("The number",check1,"is there")
# else:
#     print("Try it again")

# # Manipulate list2
# if List_input1 == "2":
#     print(list2)
# # Adding
#     if List_input2 == "+":
#         list2.insert(int(input()),int(input()))
#         print(list2)
# # removing
# elif List_input2 == "-":
#         list2.remove(int(input()))
#         print(list2)
# # put list in reverse
# elif List_input2 == "4":
#         list2.reverse()
#         print(list2)
# # Returning the entry
# elif List_input2 == "5":
#         print(list2.index(1))
# # searching for something
# elif List_input2 == "6":
#             check2 =(input("Which number are you looking for? "))
#             if check2 in list2:
#                 print("The number",check2,"is there")
# else:
#     print("Try it again")
#
# # Manipulate list1
# if List_input1 == "3":
#     print(list3)
# # Adding
#     if List_input2 == "+":
#         list3.insert(int(input()),int(input()))
#         print(list3)
# # removing
# elif List_input2 == "-":
#         list3.remove(int(input()))
#         print(list3)
# # put list in reverse
# elif List_input2 == "4":
#         list3.reverse()
#         print(list3)
# # Returning the entry
# elif List_input2 == "5":
#         print(list3.index(1))
# # searching for something
# elif List_input2 == "6":
#             check3 =(input("Which number are you looking for? "))
#             if check3 in list3:
#                 print("The number",check3,"is there")
# else:
#     print("Try it again")
