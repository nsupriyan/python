def grade(gra):
    if(gra>=90):
        print("A")
    elif(gra>=80 and gra<=89):
        print("B")
    elif(gra>=79 and gra<=70):
        print("C")
    elif(gra>=69 and gra<=60):
        print("D")
    else:
        print("F")
gra=int(input("enter ur score:"))
grade(gra)

def even(number):
    if(number%2==0):
        print("its even")
    else:
        print("its odd")
number=int(input("enter number:"))
even(number)

def tem(convert):
    if(convert<15):
        print("its cold")
    elif(convert>15 and convert<25):
        print("its moderate")
    else:
        print("its hot")
convert=int(input("enter temp:"))
tem(convert)




def traingle(angle):
    if(angle=="equailateral"):
        print("all sides are equal")
    elif(angle=="isosceles"):
        print("only two sides equal")
    elif(angle=="scalene"):
        print("only two sides equal")
    else:
        print("choose crt option")
angle=input("enter angle")
traingle(angle)

def leaf(year):
    if(year%4==0 and year%100!=0)or(year%400==0):
        print("its leaf year")
    else:
        print("its not leaf year")
year=int(input("enter year"))
leaf(year)


def age(categorizer):
    if(categorizer<=12):
        print("child")
    elif(categorizer<=19):
        print("teenager")
    elif(categorizer<=60):
        print("adult")
    else:
        print("old")
categorizer=int(input("enter age:"))
age(categorizer)


def cal(a,b,oper):
    if(oper=="+"):
        print(a+b)
    elif(oper=="-"):
        print(a-b)
    elif(oper=="*"):
        print(a*b)
    elif(oper=="%"):
        print(a%b)
    else:
        print("check once")
a=int(input())
b=int(input())
oper=input()
cal(a,b,oper)

def login(email,password):
    if(email=="nsupriya2512@gmail.com" and password=="supriya"):
        print("login succesful")
    else:
        print("pls check once")
email=input("enter ur mail:")
password=input("enter ur password")
login(email,password)

def bmi(height,weight):
    a=weight%height**2
    if(a<18.5):
        print("ur underweight")
    elif(a<=18.5 and a<24.9):
        print("normal")
    elif(a<=25 and a<29.9):
        print("overweight")
    else:
        print("obese")
height=float(input("enter ur height in m"))
weight=int(input("enter ur weight in kgs"))
bmi(height,weight)
    

