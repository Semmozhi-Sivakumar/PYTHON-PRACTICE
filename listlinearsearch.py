#linear search
num = [10,20,30,40,50]
search = 30
found = True
for i in num:
    if(i==search):
        found = True
        break
if found :
    print("found")
else:
    print("Not Found")        
