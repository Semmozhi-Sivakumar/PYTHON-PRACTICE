#Find the frequency of a digit in a number.
n = int(input())
target = int(input())
count = 0
while n!=0 :
    digit = n % 10
    if(digit == target ):
        count = count + 1
    n = n // 10
print(count)            