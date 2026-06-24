#Find the HCF using a loop.
a = int(input())
b = int(input())
while b!=0:
    digit = a%b
    a = b
    b = digit
    print(a)