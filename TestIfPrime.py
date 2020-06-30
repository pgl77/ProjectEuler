print("enter number to test for primality")
x = input()
j=2
while x > j:
    if x%j==0 and j!=x:
        print j, x, " is not prime"
        break
    j=j+1
else:
    print j, x, " is prime"
