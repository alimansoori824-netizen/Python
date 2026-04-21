n= int(input("Enter number"))
rev,x=0,n
while n>0:
    ld=n%10
    rev=rev*10+ld
    n=n//10

if(x==rev):
    print("Palindrome")

else:
    print("not a Palindrome")
