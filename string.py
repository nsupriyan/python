# Even or Odd Checker:
# Take an integer as input and print whether it's even or odd.
# ip=4
# if(ip%2==0):
#     print("even")
# else:
#     print("odd")
# Sum of Digits:
# Given a number, find the sum of its digits (e.g., 123 ➝ 6).
# num=int(input("a"))
# sum = 0
# while(num>0):
#     sum += num%10
#     num //= 10
# print(sum)
# Count Vowels in a String:
# Input a string and count how many vowels it contains.
# ip=input("enter a string")
# count=0
# for x in ip:
#     if x.lower() in "aeiou":
#         count+=1
# print(count)
# Check Palindrome:
# Check if a given string or number is a palindrome (same forward and backward).
# def palindrome(str):
#     op = ""
#     for x in range(len(str)-1,-1,-1):
#         op += str[x]
#     print(op)
#     if(str == op):
#         print(f" {str} is palindrome")
#     else:
#         print(f" {str} is not a palindrome")
# str = input("Enter String: ")
# palindrome(str)
# Find Maximum in a List:
# Given a list of numbers, find and print the maximum number.
# list1=[12,13,14]
# print(max(list1))
# Reverse a String Without Using [::-1]:
# Reverse a string using a loop or recursion.
# str="egg"
# op1 = ""
# for x in range(len(str)-1,-1,-1):
#     op1 += str[x]
# print(op1)
# Count Frequency of an Element in a List:
# Input a list and an element; count how many times the element appears.
# list3=[1,2,2,2,2,3,3,3,3,3,3,3,8,9,0,0,0,0,1]
# ele1=int(input("enter"))
# count1=(list3.count(ele1))
# print(count1)
# Print First N Prime Numbers:
# Take N as input and print the first N prime numbers.
# n=int(input("enter a value"))
# num=2
# while n>0:
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)
#         n-=1
# num+=1   
# Remove Duplicates from a List:
# Given a list, return a new list without duplicates (maintain order).
# l1=[1,1,1,2,2,2,2,2,2,2,2,5,5,5,5,5,0,0,0,0]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append (i)
# print(l2)
# FizzBuzz:
# For numbers from 1 to N, print:

# “Fizz” if divisible by 3

# “Buzz” if divisible by 5

# “FizzBuzz” if divisible by both

# Else print the number itself.
# N = int(input("Enter a number: "))
# for i in range(1, N + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
