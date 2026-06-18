#Find the sum of digits of a number.
n = int(input())
sum = 0
while (n>0):
    digit = n % 10
    sum = digit + sum
    n = n // 10
print(sum)    