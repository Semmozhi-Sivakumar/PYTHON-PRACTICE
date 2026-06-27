#Find factorial using while.
n = int(input())
fact = 1
while n!=0:
    fact = n*fact
    n= n-1
print(fact)
