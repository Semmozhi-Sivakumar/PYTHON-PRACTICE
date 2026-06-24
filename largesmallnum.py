#Find the largest and smallest digit in a given number.
n = int(input())
smallest = 9    # largest = 0 
while (n >0):
    digit = n % 10
    if(digit < smallest):  # digit > largest
        smallest = digit
    n = n // 10
print(smallest)        # largest 
 

    
    
