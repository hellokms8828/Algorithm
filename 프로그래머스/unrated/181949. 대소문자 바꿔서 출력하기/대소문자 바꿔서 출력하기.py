str = input()
result=""
for i in str:
    if(i.isupper()):
        result+=i.lower()
    else:
        result+=i.upper()
print(result)