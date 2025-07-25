# n=11
# for i in range(2,n):
#     if n%i==0:
#         print("its not prime")
#         break
# else:
#     print("prime")

# n1="silent"
# n2="listen"
# a=sorted(n1)
# b=sorted(n2)
# if a==b:
#     print("its anagramas")
# else:
#     print("not")

# lst = [10, 20, 5, 8]
# largest = second = -1 
# for num in lst:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num
# print(second)

n=6
l1=[1,2,5]
for i in range(1,6):
    if i not in l1:
        print(i)