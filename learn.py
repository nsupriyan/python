def sample():
    print("hi")
sample()

def evenodd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")
evenodd(10)

def greet(name):
     print(f"good mrng: {name}")
greet("priya")

def my(x,y):
    return(x*y)
print(my(4,5))


def our(name,age,location="nellore"):
    return(f"{name},{age},{location}")
print(our("aakash",31))

def num(*numbers):
    return(numbers)
print(num(1,7,8,9,2,6))

def odd(name,age,location):
    return(f"{name}\n{age}\n{location}")
print(odd("priya",26,"nlr"))

def tour(*places):
    return(places)
print(tour("ap","bohar","mp"))

def position(**x):
    return(x)
print(position(name="su",age=12,location="nellore",institute="10k",course="btech"))