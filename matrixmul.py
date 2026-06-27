#Print a multiplication matrix (nested loops).
n = int(input())
m = int(input())
for i in range(1,n+1):
    for j in range(1,m+1):
        k = i*j 
        print(k,end=" ")
    print()


    
