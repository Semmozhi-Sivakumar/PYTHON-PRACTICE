#Find the strong number of a given number.
n = int(input())
original = n
sum = 0
while n > 0:
    digit = n % 10
    fact = 1
    for i in range(2,digit+1):
        fact = fact*i
    sum = sum + fact
    n = n // 10
if (sum==original):
    print ("num strong number") 
else:
    print("the num is not strong number")

