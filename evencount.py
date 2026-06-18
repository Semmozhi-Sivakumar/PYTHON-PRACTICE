#Count how many even numbers are between 1 and n.
n =int(input())
count = 0
for i in range (1,n+1):
    if (i%2==0):
        count +=1
print(count)

