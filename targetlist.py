#Find pairs whose sum equals a target.  Input: 2 7 11 15 target = 9 output : 2 7
num = list(map(int,input().split()))
target = int(input())
total =[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]+num[j]==target):
           total.append(num[i])
           total.append(num[j])
print(total)            

