# b=complex(4,5)
# print(b)
# print(abs(-88))
# li=[3,-9,0,-88,7,-95,-7]
# for x in li:
#     if(x==abs(x)):
#         print(x)
# print(pow(9,8))
# print(divmod(9000,899))
# print(round(9.9875,2))
# li=[9.086,7.986,6.983]
# for x in li:
#     print(round(x,2))
import math
#truc
# print(math.trunc(9.08))
#ceil
# print(math.ceil(6.89))
# print(math.ceil(-8.0))
#floor
# print(math.floor(9.8))
# print(math.floor(-10.78))
#fab
# print(math.fabs(-4.89))
import random
# print(random.randint(9000,8000000))
# print(random.random())
# print(random.uniform(1,3))
# li=[1,2,3,4,5,6.90,7]
# print(random.choice(li))
#string methods
#lower
# a="SUPRIYA"
# b=a.lower()
# print(b)
# k=["HELLO","hi","PYTHON","css","js","react","DJANGO"]
# for a in k:
#     if a==a.lower():
#         print(a)
# for a in k:
#     if a==a.upper():
#         print(a)
# s="krsna"
# b=s.capitalize()
# print(b)
# b1="india iss my  country ,all indians are "
# c=b1.title()
# print(c)
# s1="AN APPLE KEEPS A DOCTOR a way"
# d=s1.swapcase()
# print(d)
# f="     supriya        "
# e=f.strip()
# print(e)
# g="supriya"
# h=g.replace("su"," ")
# print(h)
# h="door"
# i=h.find("o")
# print(i)
# h1="python is easy lang"
# h2=h1.find("easy")
# print(h2)
# h3="develop"
# op=h3.rfind("e",3,5)
# print(op)
# h="ddddaaaoooooopppppppddd"
# op=h.count("o")
# print(op)
# j="supriya"
# j1=j.startswith("s")
# print(j1)
# j="supriya"
# j1=j.endswith("a")
# print(j1)
# kk="supppppp1111"
# k1=kk.isalnum()
# print(k1)
# l2=[2,3,4,5,6,7]
# l2.append(90)
# print(l2)
# l2="s_o_m_e"
# s=l2.split("_")
# print(s)
# mul_str="""hello
# 45r
# welcome"""
# s1=mul_str.splitlines()
# print(s1)
# seq={"js","python","sql"}
# dd="why".join(seq)
# print(dd)
# lo=[2,3,4,5,6,7]
# lo.extend((9,8,0,0,9))
# print(lo)
# j=[2,3,4,5,6,7]
# j.insert(2,90)
# print(j)
# j=[2,3,4,5,6,7]
# j.remove(4)
# print(j)
# j=[2,3,4,5,6,7]
# j.pop(1)
# print(j)
# j=[2,3,4,5,6,7]
# j.clear()
# print(j)
# nums=[45,34,12,13,19,49]
# op=nums.sort() #it will do ascending
# nums.sort(reverse=True) #it will do descending
# print(nums)
import copy
# shallow copy and deep copy.
# ip1=[[1,2],[5,6]]
# ip2=ip1.copy()


# ip2[0][1]="hi"

# print(ip1,ip2)

# ip1=[["hi","hello"],["js","python"]]
# ip2=copy.deepcopy(ip1)

# ip2[0][1]="bye"

# print(ip1,ip2)