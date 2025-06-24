def match_status(team,match_won):
    if(match_won):
        print(f"{team} won the match")
    else:
        print(f"{team} lost the match")
match_status("RCB",True)
match_status("PBKS",False)
match_status("SRH",True)
match_status("MI",False)

def login(email,password):
    if(email==True and password==True):
        print("true")
    else:
        print("false")
login(True,False)
login(True,True)
login(False,False)
login(False,False)


a=10
b=20
if(a>b):
    print("true")
else:
    print("false")


def even(x):
    if(x%2==0):
        print("its even")
    else:
        print("its odd")
even(7)

def gre(a,b):
    if(a>b):
        print(f"{a} is greater")
    else:
        print(f"{b} is greater")
gre(9,10)


def gre1(name,a):
    if(a>35):
        print(f"{name} {a} cleared exam")
    else:
        print(f"{name} {a} not cleared exam")
gre1("priya", 50)
gre1("aakash",34)

def gre2(name,a):
    if(a>18):
        print(f"{name} {a} eligible for vote")
    else:
        print(f"{name} {a} not eligible for vote")
gre2("priya", 50)
gre2("aakash",14)

def gre3(a):
    if(a>0):
        print(f" {a} positive")
    else:
        print(f" {a} negative")
gre3(50)
gre3(-34)


def length(a):
    if len(a)>=8:
        print("it is validated")
    else:
        print("not validated")
length("priya")

def length1(a):
    if len(a)%2==0:
        print("it is even")
    else:
        print("odd")
length1("priya")


def discount(price):
    if price>=1000:
        dis=price*(10/100)
        print("u got discount")
    else:
        print("not discount")
discount(10000000000)

def num(number):
    if(number>0):
        print("positive")
    elif(number<0):
        print("negative")
    else:
        print("zero")
num(0)

def eamcet(rank):
    if(rank<10000):
        print("got seat in jntua")
    elif(rank>10000 and rank<25000):
        print("got seat in mallareddy")
    elif(rank>25000 and rank<50000):
        print("got seat in svcn")
    else:
        print("got seat in naryana")
rank=int(input("enter rank:"))
eamcet(rank)


def log(login,user):
    if(login==True):
        if(user=="admin"):
            return "welcome admin"
        else:
            return "welcome student"
    else:
        return "login fst"
print(log(True,"admin"))




    
    
     







