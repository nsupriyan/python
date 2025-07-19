# def addf(num1,num2):
#     return num1+num2
# print(addf(1,2))

# def mulf(a,b):
#     return a*b
# print(mulf(9,3))

# def facc(n):
#     a=n*(n-1)
#     return a
# print(facc(3))

# def gree(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(gree(1,4))

# def evef(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(evef(3))

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# # Example usage
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

# def maxf(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(max(2,3,4))

# def revf(n):
#     rev=0
#     while n>0:
#         d=n%10
#         rev=rev*10+d
#         n=n//10
#     return rev
# print(revf(9876))
 
# def counnf(num):
#     count=0
#     for i in str(num):
#         count+=1
#     return count
# print(counnf(7445))

# def celsiusfarhen(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# print(celsiusfarhen(270))
    
# def leaf(year):
#     if(year%4==0 and year%100!=0)or(year%400==0):
#         print("its leaf year")
#     else:
#         print("its not leaf year")
# year=int(input("enter year"))
# leaf(year)

# def hoursf(num):
#     hours=num//60
#     min=num%60
#     return hours,min
# print(hoursf(345))
   

# def factors(n):
#     result = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             result.append(i)
#         max=result[0]
#     for i in result:
#         if i>max:
#             max=i
#         lcm=1
#     for i in result:
#         lcm*=i
#     return result,max,lcm
# print(factors(65))



# def mulf(n):
#     result='' 
#     for i in range(1,11):
#         result+=str(n*i)
#     return result
# print(mulf(4))

# def avef(l1,l):
#     sum=0
#     for i in range(1,len(l1)):
#         sum+=l1[i]
#         ave=sum/l
#     return ave
# l1=[1,2,3,4]
# l=len(l1)
# print(avef(l1,l))

# def naag():
#     name=(input("name"))
#     age=int(input("enter age"))
#     return (f"{name} and ur {age}")
# print(naag())

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)  # prints first 10 Fibonacci numbers


