a=int(input())
f=0
for i in range(2,a):
    if a%i==0:
        f=1
        print("it is divided by",i)
        break
if f==1:
    print(a,"is not a prime number")
else:
    print(a,"is a prime number")
    c=a
    rev=0
    while c>0:
        r=c%10
        rev=rev*10+r
        c=c//10
    print("reverse of a is ",rev)
    if a==rev:
        print(a,"is a palindrome number")
    else:
        print(a,"is not a palindrome number")
