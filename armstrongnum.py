#Check whether a number is an Armstrong number (3-digit first).
m = int(input())
original = m # original value should be assigned to store the actual m value to compare .
n = str(m)
sum = 0
power = len(n)
while(m>0):
    digit = m % 10
    sum = digit**power + sum
    m = m // 10
if(original==sum):
    print(f"{sum}\nit is a armstrong number") 
else:
    print(f"{sum}\nit is not a armstrong number")      
