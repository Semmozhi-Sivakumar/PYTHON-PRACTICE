#Reverse a list without using reverse().
num = list(map(int,input().split())) # 10 ,20, 30, 40
rev_list=[]
for i in range(len(num)):
    x=num[len(num)-1-i]
    rev_list.append(x)
print(rev_list)