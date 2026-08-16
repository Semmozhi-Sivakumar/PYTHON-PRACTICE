#Move all odd numbers to the beginning. 10 15 20 7 8 9
num = list(map(int,input().split()))
odd = []
nums = []
for i in num:
    if(i%2!=0):
        odd.append(i)
    else:
        nums.append(i)
print(odd+nums)            

