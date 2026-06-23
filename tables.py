#Multiplication table of a number.
a = int(input())
n = int(input())
table = 0
for i in range(1,n+1):
    table = a * i
    print (a ,"x" , i , "=" , table)

