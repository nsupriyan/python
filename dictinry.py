# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# c= list(set(list1) & set(list2))
# print(c)



# [4, 5]

# Create a list of numbers divisible by both 3 and 5 between 1 and 20.
# res=[x for x in range(1,20) if x%3 == 0 and x%5 == 0]
# print(res)

# [15]

# Get all palindrome words from a list.
# l1=['apple', 'window', 'python', 'garden', 'madam', 'level', 'radar', 'Wow','Mom']
# count=0
# for i in l1:
#     i=i.lower()
#     if i == i[::-1]:
#         count += 1
# print(count)
       

# 5

# Create a list of ASCII values for all characters in a string
# str1="Python Language"
# res=[ord(x) for x in str1]
# print(res)

# [80, 121, 116, 104, 111, 110, 32, 76, 97, 110, 103, 117, 97, 103, 101]

# Reverse each word in a given list of strings

# str1 =["Sriyha","Sarada","sandhya","shyamala","Suvarna","Sujatha","Samskirthi"]
# res = [x[::-1] for x in str1]
# print(res)

# ['ahyirS', 'adaraS', 'ayhdnas', 'alamayhs', 'anravuS', 'ahtajuS', 'ihtriksmaS'] 


# Find all prime numbers in a given list. input for this? 
# l1= [3, 4, 7, 10, 13, 17, 20, 23, 28, 29, 30, 37]
# res = [x for x in l1 if all(x%y != 0 for y in range(2,x))]
# print(res)

# [3, 7, 13, 17, 23, 29, 37]

# Find Max and Min Value in Dictionary Input: d = {'a': 10, 'b': 5, 'c': 15} Output: Max Value → 15 Min Value → 5

# d = {'a': 10, 'b': 5, 'c': 15}
# max = max(d.values())
# min = min(d.values())
# print("Max number :",max)
# print("Min number:", min)

# Max number : 15
# Min number: 5

# Input:[[1,2,3],[4,5,6]]    output: [1,2,3,4,5,6]
# l2 = [[1, 2, 3], [4, 5, 6]]
# res= [x for y in l2 for x in y]
# print(res)

# [1,2,3,4,5,6]