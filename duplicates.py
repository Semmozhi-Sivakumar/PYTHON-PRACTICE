#21. Remove duplicates without using set().
num = list(map(int,input().split())) # 10 20 20 30 40 
unique  = []
for i in num:
    if i not in unique:
        unique.append(i)
print(unique)    
    

