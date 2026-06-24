#Find the product of digits of a number.
n = int(input())
product = 1
while n>0 :
    digit = n % 10
    product = digit*product
    n = n // 10
print(product)