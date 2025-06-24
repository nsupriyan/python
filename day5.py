list=["apple", "mango", "pineapple", "watermelon", "orange", "blueberry", "banana"] 
# print fruits which having even number length from above list of fruits. 
for i in list:
    if(len(i)%2==0):
        print(list)

#From the list of fruits, print only those that contain the letter 'e'. 

for r in list:
    if "e" in r:
        print(r)

employee_details=[ 
{'name': 'Mounika', 'salary': 29000, 'role': 'HR'}, 
{'name': 'Sreeja', 'salary': 32000, 'role': 'Developer'}, 
{'name': 'KiranKumar', 'salary': 35000, 'role': 'HR'}, {'name': 'Rajesh', 'salary': 28000, 'role': 'Developer'}, 
{'name': 'Anusha', 'salary': 31000, 'role': 'Tester'}, 
{'name': 'Vikram', 'salary': 34000, 'role': 'Manager'}, 
{'name': 'Trinath', 'salary': 30000, 'role': 'HR'} ]
 
#PRINT EMPLOYEE DICTIONARY WHERE SALARY >=30000 AND ROLE IS HR 
for emp in employee_details:
    if (emp['salary']>=30000 and emp['role']=='HR'):
        print(emp)

for emp1 in employee_details:
    if emp1['name'][0] in ('A', 'E', 'I', 'O', 'U') and emp1['salary'] > 30000:
        print(emp1['name'])

list=[23,25,28,34,35,38,39,40,42,108,112]
for i in list:
    if i%3==0:
        print(i)

