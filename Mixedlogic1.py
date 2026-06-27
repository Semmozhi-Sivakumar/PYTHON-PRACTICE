#Find the second largest number (without using lists, use user input).
n = int(input())
largest = 0
second_largest = 0
count = 0
while count < n:
    num = int(input("enter the number:"))
    if(num>largest):
        second_largest = largest
        largest = num
    elif(num>second_largest):
        second_largest = num
    count = count + 1
print(second_largest)  
