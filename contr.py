x= ["html", "css", "js", "react", "python", "django"]
i = 0
print("Even :")
while i < len(x):
    if len(x[i]) % 2 != 0:
        i += 1
        continue
    print(x[i])
    i += 1
i = 0
print("Odd :")
while i < len(x):
    if len(x[i]) % 2 == 0:
        i += 1
        continue
    print(x[i])
    i += 1