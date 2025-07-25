# dict1={}
# name=input("enter name")
# marks=int(input("enter marks"))
# dict1[name]=int(marks)
# type=input("type here")
# if (type=="stop"):
#     print(dict1)

# n=[1,[2,3],[4,[5]]]
# list1 = []
# def flatns(n):
#     for item in n:
#         if isinstance(item, list):
#             flatns(item) 
#         else:
#             list1.append(item)
# flatns(n)
# print(list1)

# a=[1,1,1,1,1,2,2,2,2,2,2,4,4,4,4,3,3,3,3,3,3,5,5]
# count=0
# b={}
# for i in a:
#     if i==a:
#         count+=1
#     else:
#         count=1
# b[a]=(count)
# print(b)

# my_list=[]
# def add_items():
#     item = input("Enter a number to add: ")
#     my_list.append(item)
#     print("Added sucessfully")
# def remove_item():
#     item = input("Enter a number to remove")
#     if item in my_list:
#         my_list.remove(item)
#         print("Removed")
#     else:
#         print("Not found")
# def display():
#     if my_list:
#         print(my_list)
#     else:
#         print("U r list is empty")
# while True:
#     print("Menu")
#     print("1. Add item")
#     print("2. Remove item")
#     print("3. Display list")
#     print("4. Exit")
#     ip=input("Enter choice (1-4): ")
#     if ip == '1':
#         add_items()
#     elif ip == '2':
#         remove_item()
#     elif ip == '3':
#         display()
#     elif ip == '4':
#         print("Exit!")
#         break
#     else:
#         print("Invalid choice.")

# Input=[1, 3, 2, 2, 4, 0,8,9]
# target=17
# output=[]
# for i in range(len(Input)):
#     for j in range(i+1,len(Input)):
#         if Input[i]+Input[j]==target:
#             output.append((Input[i],Input[j]))
# print(output)




# , target = 4 → Output: [(1,3), (2,2), (4,0)]
