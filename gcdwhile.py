#Find GCD using while.
n = int(input())
m = int(input())
gcd = 1
while m != 0:
    digit = n % m
    n = m
    m = digit
print(n)    
