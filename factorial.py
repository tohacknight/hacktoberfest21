n=int(input("Enter your number :"))

fact=1

if n==0:
    print('Factorial of 0 is 1')

elif n<0:
    print("you have entered a negative number")

if n>0:
    for i in range(n):
        fact=fact*n
        n=n-1
    print("Factorial of given number is ",fact)