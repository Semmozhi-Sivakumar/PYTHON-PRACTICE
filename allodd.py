#Print all odd numbers from 1 to n.
n = int(input("enter a number: "))
for i in range (1, n+1):
    if(i%2!=0):
        print(i)