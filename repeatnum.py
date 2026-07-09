# Count how many times a number appears
numbers = [10,20,30,20,40,20]
repeat = int(input())
count = 0
for i in numbers:
    if(i==repeat):
        count+=1
print(count)        
