#Count the number of digits in an integer.
n=int(input())
count=0
while(n>0):
    count = count+1
    n = n // 10
print(count)

