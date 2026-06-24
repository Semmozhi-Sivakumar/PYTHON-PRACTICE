#Count how many prime numbers exist from 1 to n.
n = int(input())
count = 0
for num in range(2,n+1):
    is_prime = True
    for i in range(2,num):
        if(num%i==0):
            is_prime = False
            break
    if(is_prime == True):
        count+=1
print(count)

