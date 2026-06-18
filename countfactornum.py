#Count the number of factors.
n = int(input())
count = 0
for i in range(1,n):
    if (n%i==0):
        count=count+1
print(count,"are the count of the given factor")        