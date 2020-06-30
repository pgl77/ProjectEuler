print("How many primes do you want?")
N = input()
a = 2
while a < N:
    a =a+1
    j=2
    x=a
    while x > j:
        if x%j==0 and j!=x:
            #print x, " is not prime, divisible by ", j
            break
        j=j+1
    else:
        print j,# " is prime, divisible by 1 and itself", x
