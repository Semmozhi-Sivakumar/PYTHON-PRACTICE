#22. Find the frequency of every element.

num = list(map(int,input().split())) #10 20 20 30 10
freq = []
for i in num:
    if i not in freq:
        count = 0
        for j in num:
            if(i==j):
                count+=1
        print(i,count)
        freq.append(i)        


