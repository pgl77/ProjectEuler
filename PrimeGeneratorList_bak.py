#!/usr/bin/python3

# Prime number generator using txt file with primes in already
# OPEN FILE WITH primes
import datetime
import sys

primes = []
sum = 0
infile = open("output.txt", 'r')
primes = infile.read().splitlines()
# using list comprehension to
# perform conversion
primes = [int(i) for i in primes]
for i in primes:
    sum += i
# print(primes)
print("----------------")
print(sum)
print(primes[-1])
# Having imported prime list, use it to determine next prime
print("Look for primes up to (which number)?")
N = int(input())
begin_time = datetime.datetime.now()
print("OK, look for primes up to: ", N)
def CheckAgainstPrimesTxt(fN):
    if fN <= int(primes[-1]):
        print('We already calculated that prime, look it up ;)')
        print(fN) #fN, "is less than ", primes[-1])
        #stretch could be to calc and print nearest prime
        sys.exit()
        return
#call function and check if we already have prime in list
CheckAgainstPrimesTxt(N)
print('Number is not in primes we have already, so calculating (please wait)...')
print("started at :", begin_time)
#use prime number list to test for primality
# Start from last number in primes list and add 2
a = primes[-1]
j=0
while a < N:
    a = a+2
    x=a
    print("I:a,x,j",a,x,j, N)
    StopPoint1 = input()
    for j in primes:
        print("Ii:a,x,j",a,x,j, N)
        StopPoint1 = input()
        if x%j==0 and j!=x:
            print(x, " is not prime, divisible by ", j)
            print("II:a,x,j",a,x,j,N)
            StopPoint2 = input()
            break
        print(x, " is prime, divisible by 1 and itself", x)
    primes.append(x)
    # maybe revisit appending prime to file each time? (only works if I=O file)
    # MyFile.write(str(x))
    # MyFile.write('\n')
TimeTaken = datetime.datetime.now() - begin_time
# print(datetime.datetime.now() - begin_time)
print(primes[-1])
print("primes finish calculation at: ", datetime.datetime.now())
print(TimeTaken)
MyFile=open('output.txt','w')
for element in primes:
     MyFile.write(str(element))
     MyFile.write('\n')
MyFile.close()
print("output file updated at : ", datetime.datetime.now())
