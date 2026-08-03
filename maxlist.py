#Find the maximum difference between two elements.
num =  list(map(int,input().split())) # 10 40 15 30
largest = 0
smallest = 10
for i in num:
    if i > largest:
        largest = i
    if i < smallest :
        smallest = i
difference = largest - smallest
print(difference)            

