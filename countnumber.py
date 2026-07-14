# Count how many times a number appears.
numbers = [10,20,30,20,40,20]
count = 0
search = int(input("Enter a number :"))
for i in range(len(numbers)):
    if search == numbers[i]:
        count +=1
print(count)            

