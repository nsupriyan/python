x=10
def show():
    x=5
    print(x)
show()
print(x)

#x=5 is inside the function show(), so it is a local variable, and 5 is printed first.

#x =10 is inside outer() function, and inner() is also inside outer() function. 15


def outer():
    x=10
    def inner():
     print(x)
    inner()
outer()

#inner() function doesn't have any x value, it uses x value from outer() funtion, so it prints 10,
 
#10 is a global variable, so it is printed outside the function.



x="global"
def outer():
    x = "outer"
    def inner():
        x = "inner"
    inner()
    print("outer:",x)
outer()
print("global:",x)

# x "global" is a global variable.

#inside outer() function, x = "outer" is a local variable to outer(). 27

#inside inner() function, x = "inner" is a local variable to inner() only. It will not change the x value in outer(). 28

#outside, print("global:", x) prints "global from the global variable. 30
 #then print("outer:", x) runs, it prints "outer" because x in outer() remains unchanged.

    