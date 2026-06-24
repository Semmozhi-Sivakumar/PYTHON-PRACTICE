#Check whether two numbers are co-prime.
n = int(input())
m = int(input())
gcd = 1
for i in range (1,min(n,m)+1):
    if(n%i==0 and m%i==0):
        gcd = i
if(gcd == 1):
    print(f"{gcd}the number is co-prime")
else:
    print(f"{gcd}the number is not co-prime ")    
