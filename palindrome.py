#Check whether a number is a palindrome
n = int(input())
original = n
reverse = 0  
while n>0:
    digit = n % 10
    reverse = reverse * 10 + digit  ##it is used to store digit and make place for another digit if n % 10 i.e (121%10) => 1
    n = n // 10                      ## reverse = 0 *10 + 1(digit=1) =>0+1=>1 . => reverse=1 
if(reverse == original ):               ## second iteration => reverse = 1*10 + 2  ==>10+2 ==>12 .....and so on 
    print(f"{reverse} \nis a palindrome number")        
else:
    print(f"{reverse} \nis not a palindrme number")                          