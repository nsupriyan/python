# Retrieve string even index characters in list,
# s="supriya"
# a=[s[i]for i in range(0,len(s),2)]
# print(a)
 

# s= ["even_index", True, 3.4, 3+6j, "reverse"]  


# 3. Write a Python script to separate upper case letters and 
# lower case letters from a given string. Also form a sentence 
# to explain what your code does.
# str1="PythoNFullStacK" 
# upper_let=[i for i in str1 if i.isupper()]
# lower_let=[j for j in str1 if j.islower()]
# print(upper_let)
# print(lower_let)

# 4. Swap the case of all letters in a string. 
# s="AASSSbbbnnnnmk"
# for i in s:
#     b=s.swapcase()
#     print(b)

# 5. Remove duplicates from a list while preserving order.
# a=[1,1,1,1,2,2,4,5,6]
# b=[]
# for i in a:
#     if i not in b:
#         b+=[i]
# print(b)

# 6. Find the largest and smallest number in a list. With out using 
# built in method? 
# a=[1,2,3,4,5]
# max=a[0]
# min=a[0]
# for i in a:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
# print(min)
# print(max)
  
# 7. Separate a list into two lists — positives and negatives. 
# l=[1,2,3,4,5,6,-1,-2,-5,-6]
# a=[]
# b=[]
# for i in l:
#     if i>0:
#         a+=[i]
#     else:
#         b+=[i]
# print(a)
# print(b)


# 8. Retrieve all elements at odd indices in a list. 
# a=[1,2,3,4,5]
# b=[]
# for i in range(1,len(a),2):
#     b+=[i]
# print(b)


# 9. Multiply all elements in a list together. 
# l=[2,3,4,5,6]
# mul=1
# for i in l:
#     mul*=i
# print(mul)

# 10. Sort a list of numbers in ascending order without using 
# sort() or sorted().
# my_list = [5, 2, 9, 1, 5, 6]


# n = len(my_list)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if my_list[j] > my_list[j + 1]:
          
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

# print(my_list)
# # 11. Write a Python code to add an underscore ‘@’before each 
# # capital   letter in a given string Reverse a list without using 
# # reverse() or slicing. 
# text = "Python"
# result = ""

# for char in text:
#     if char.isupper():
#         result += '@' + char
#     else:
#         result += char

# print("Modified string:", result)

# # 12. Write python code to find the nearest prime number to a 
# # given number
# n=8
# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(n)
# else:
#     a = n - 1
#     b = n + 1

#     is_a_prime = True
#     for j in range(2, a):
#         if a % j == 0:
#             is_a_prime = False
#             break
#         if is_a_prime:
#             print(a)
#         break

#     is_b_prime = True
#     for k in range(2, b):
#         if b % k == 0:
#             is_b_prime = False
#             break
#         if is_b_prime:
#             print(b)
#             break