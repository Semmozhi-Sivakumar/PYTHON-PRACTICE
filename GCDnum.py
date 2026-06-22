#Find the GCD (Greatest Common Divisor) of two numbers.
n = int(input())
m = int(input())
for i in range(1,min(n,m)+1):
    if(n%i==0 and m%i==0):
        gcd = i
print(gcd)  
