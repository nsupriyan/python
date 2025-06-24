a=4
b=9
print("a is big") if a>b else print("b is big")

a=3
b=4
c=5
if(a>b and a>c):
    print("a is big")
elif(b>a and b>c):
    print("b is big")
else:
    print("c is big")

def ten(a,b,c):
    if(a>b and a>c):
        print("a is big")
    elif(b>a and b>c):
        print("b is big")
    else:
        print("c is big")
ten(11,7,8)
'''a=9
b=8
c=11
lar= a if (a>b and a>c)  else b (b>a and b>c) else c
print({lar})'''
for i in range(11):
    print(i)
 
for i in range(0,20,2):
 print(i)

for i in range(5,50,5):
    print(i)

n= int(input("Enter"))
for i in range(11):
    print(f"{n} * {i} = ",n*i)


for i in range(1,11):
    print(f"2x{i}=2*{i}")

def table(n):
    for i in range(11):
        print(f"{n} * {i} = ",n*i)
n= int(input("Enter"))
table(n)


for i in range(1,10):
    print("*" *i)
    
    






