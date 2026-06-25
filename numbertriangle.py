#Print a number triangle:
n = int(input())
for i in range(0,n+1):
    for j in range(i+1):
        print(j+1,end="")
    print()