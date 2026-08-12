#Find the smallest even number  15 8 21 4 11 6
num = list(map(int,input().split()))
even = []
small = 10
for i in num:
    if(i%2==0):
        even.append(i)
for i in even:
    if(i<small):
        small = i
print(small)                
