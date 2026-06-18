#Find all factors of a given number.
n = int(input())
for i in range(1,n):
    if(n%i==0):
        print(i ,"are the factors of a given number")