sample=lambda x,y : x*y
print(sample(2,3))

sample=lambda a,b : a/b
print(sample(10,5))

sample=lambda a,b : a//b
print(sample(20,10))

sample=lambda a,b: a+b
print(sample(9,10))

pi=3.14
def circle():
    r=3
    def area():
        unit="cm"
        a=pi*r*r 
        print(f" {a }{unit}")
    area()
circle()


pi=3.14
def semi():
    r=34
    def area():
        unit="cm "
        f=pi*r*r/2
        print(f"{f} {unit}")
    area()
semi()

name="aakash"
def greeting():
    x="good mrng"
    def show():
        s="hello"
        print(s+x+name)
    show()
greeting()