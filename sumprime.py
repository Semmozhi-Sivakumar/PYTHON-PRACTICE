#Find the sum of all prime numbers from 1 to n.
n = int(input())
sum = 0
for num in range(2,n+1):
    is_prime = True
    for i in range(2,num):
        if(num%i==0):
            is_prime = False
            break
    if(is_prime):
        sum = num + sum
print(sum)        