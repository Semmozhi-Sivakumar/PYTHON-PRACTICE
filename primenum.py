#basic prime 
#n = int(input())
#for i in range(2,n):
#    if(n%i==0):
#        print("not prime")
#else:
#    print("prime")        

# better version prime number program.
n = int(input())
is_prime = True 
if (n<=1):
    is_prime = False
else:
    for i in range(2,n):
        if(n%i==0):
            is_prime  = False
            break
if is_prime :
    print("the number is prime number")
else:
    print("the number is not a prime number")    
      
