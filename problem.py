# EVEN AND ODD (DIFF LOGIC)             
# num=891
# if num & 1 == 0:
#     print("EVEN")
# else:
#     print("ODD")rted[i]
# print(rev)
# if rev==str(num2):
#     print("palindrome")
# else:
#     print("not")

# n=1234
# rev=0
# while n>0:
#     id=n%10
#     rev=rev*10+id
#     n=n//10
# print(rev)

# n = 13
# count = len(str(n))
# sum = 0
# temp = n
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** count
#     temp = temp // 10
# if sum == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# n = 153
# count = len(str(n))
# sum = 0

# for digit in str(n):
#     sum += int(digit) ** count

# if sum == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# str1="school"
# count=0
# extrachar="o"
# for char in str1:
#     if(char==extrachar):
#         count+=1
# print(count)

# numm=99999
# count=0
# cnvrt=str(numm)
# for i in cnvrt:
#     if int(i)==9:
#         count+=1
# print(count)

# numbe=1234444432
# seaarchd=4
# count=0
# while numbe>0:
#     id=numbe%10
#     if(id==seaarchd):
#         count+=1
#     numbe=numbe//10
# print(count)

# n1=153
# cubes=0
# sum=0
# while n1>0:
#     lastdigit=n1%10
#     cubes+=lastdigit**3
#     n1=n1//10
# print(cubes)

# list1 = [4,7,1,2,8,9,10,1,3]
# max = list1[0]
# for num in list1:
#     if num > max:
#         max = num
# print(max)

# n=15
# a,b=0,1
# for i in range(n):
#     print(a)
#     a,b=b,a+b

# n=6
# fac=1
# for i in range(1,n+1):
#     fac*=i
# print(fac)

# str11="supriya"
# for char in range(len(str11)-1,-1,-1):
#     print(str11[char])

# stq="wow"
# l=len(stq)
# s=""
# for char in range(l-1,-1,-1):
#     s+=stq[char]
# if(s==stq):
#     print("palindrom")
# else:
#     print("not")

# d="good"
# count=0
# for char in d:
#     if char in ("a","e","i","o","u"):
#         count+=1
#         print(char,count)

# a=10
# b=5
# a,b=b,a
# print(a,b)


# l1=[0,2,4,6,8]
# num1=346
# cnvrted=str(num1)
# if int(cnvrted[-1]) in l1:
#     print("even")
# else:
#     print("odd")

# num2=181
# cnvrted=str(num2)
# rev=''
# for i in range(len(cnvrted)-1,-1,-1):
#     rev=rev+cnv
# l1 = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
# l2 = []

# for w in l1:
#     if w not in l2:
#         l2 += [w]   # Convert w to list, then use +=

# print(l2)

# lst = [5, 3, 8, 1, 2]

# n = len(lst)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if lst[j] > lst[j + 1]:
#             # swap
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]

# print("Sorted List:", lst)

# s1="silent"
# s2=[]
# for s in s1:
#     s2+=[s]
#     s2.sort()
#     print(s2)
    
# s3="listen"
# s4=[]
# for c in s3:
#     s4+=[c]
#     s4.sort()
#     print(s4)
# if s2==s4:
#     print("true")
# else:
#     print("false")

# ab="aaaaaabbbb"
# print(ab.capitalize())

# sum=0
# n=6
# l1=[1,2,4,5,6]
# for i in l1:
#     sum+=i
# # print(sum)
# n1=n*(n+1)/2
# # print(n1)
# n2=n1-sum
# print(n2)

# l2=[1,2,3,4,5,6,7]
# l2.sort(reverse=True)
# print(l2[1])

# o="priya is more beautiful than sriyha"
# print(o.split(","))
# op=""
# for p in o:
#     op+=p
# print(op)













