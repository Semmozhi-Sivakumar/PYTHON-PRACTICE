#Check whether a number is a perfect number.
n = int(input())
total = 0
for i in range(1,n):
    if(n%i==0):
        total = total + i
if(total==n):
    print(f"{total}\n it is a number")
else:
    print(f"{total}\n it is not a perfect number")            
