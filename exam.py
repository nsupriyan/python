# n1=231
# n2=0
# org=n1
# while n1>0:
#     id=n1%10
#     n2=n2*10+id
#     n1=n1//10
# if(n2==org):
#     print("palindrom")
# else:
#     print("not")

# n=82194
# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10
# print(sum)


# num=str(234567891)
# count=0
# for i in num:
#     if int(i)%2==0:
#         count+=1
# print(count)


# n1=145
# org=n1
# fact=1
# sum1=0
# while n1>0:
#     last_digit=n1 % 10
#     for i in range(1,last_digit+1):
#         fact*= i
#     sum1+=fact
#     n1=n1 // 10
# if org == sum1:
#     print("StrongNumber")
# else:
#     print("Not")


# str = "python"
# dict = {}
# i = 0  
# j = 0  
# while j < len(str):
#     dict[i+100] = str[j]
#     i += 1
#     j += 1
# print(dict)


# x = ["a", "h", "a", "k", "j", "a", "b"]
# count_dict = {}

# for item in x:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1

# print(count_dict)

# n2="banana"
# op1={}
# for a in n2:
#     if a in op1:
#         op1[a]+=1
#     else:
#         op1[a]=1
# print(op1)


# n9="huhascscewuhfrhfhwudfieoiowejdamxmancsbcbwruerfhewiwqppwwdekfjnfbvnckmdksdkdkdmcdkmdnenffbncejjj"
# op3={}
# for b in n9:
#     if b in op3:
#         op3[b]+=1
#     else:
#         op3[b]=1
# print(op3)

# Count how many times each element occurs in a list.
# Input: ["cat", "dog", "cat", "mouse"]
# 👉 Output: {'cat': 2, 'dog': 1, 'mouse': 1}

# Input=["cat", "dog", "cat", "mouse"]
# output={}
# for r in Input:
#     if r in output:
#         output[r]+=1
#     else:
#         output[r]=1
# print(output)

# Swap keys and values in a dictionary.
# 👉 Input: {"a": 1, "b": 2}
# 👉 Output: {1: "a", 2: "b"}
# original = {"a": 1, "b": 2}
# op4 = {}

# for key, value in original.items():
#     op4[value] = key

# print(op4)

# Print all keys and values using loop.
# 👉 Input: {"x": 10, "y": 20}
# 👉 Output:
# Key: x, Value: 10  
# Key: y, Value: 20
# i1={"x": 10, "y": 20}
# o1={}
# for key,value in i1.items():
#     print(f"Key: {key}, Value: {value}")

# Check if a key exists in dictionary using loop.
# 👉 Input: "name" in {"name": "Deepthi", "age": 22}
# 👉 Output: Yes, key exists.
# my_dict = {"name": "Deepthi", "age": 22}
# search = "name"

# for keys in my_dict:
#     if search == keys:
#         print("yes")
#         break
# else:
#     print("No")

# dict1 = {"a": 1}
# dict2 = {"b": 2}
# dict1.update(dict2)
# print(dict1)

# n=int(input("number plz"))
# op={}
# for i in range(1,n+1):
#     op[i]=i*i
# print(op)

# keys = ["name", "age"]
# values = ["Swathi", 22]
# op={}
# for i in range(len(keys)):
#     op[keys[i]] = values[i]
# print(op)


    




        













