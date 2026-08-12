#Find the missing number.
num = list(map(int,input().split()))
total=sum(num)
n = 0
for i in range(len(num)):
    n=n+1
missing_num = total-n*(n+1)/2
print(missing_num)     
