#24. Move all zeros to the end.  1 0 2 0 3 4 0
num = list(map(int,input().split()))
n = []
zero = []
for i in num:
    if i != 0:
        n.append(i)
    else:
        zero.append(i)
print(n+zero)            