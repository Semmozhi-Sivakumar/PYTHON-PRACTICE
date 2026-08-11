#23. Move all even numbers to the beginning. 11 20 13 4 5 6
num = list(map(int,input().split()))
even = []
odd = []
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even+odd)        




