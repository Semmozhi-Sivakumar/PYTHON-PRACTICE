#Check whether the list is sorted.
num =[10,20,30,40]
is_sorted = True
for i in range(len(num)-1) :
    if num[i]>num[i+1]:
        is_sorted = False
        break
if is_sorted :
    print("sorted")
else:
    print("Not sorted")        