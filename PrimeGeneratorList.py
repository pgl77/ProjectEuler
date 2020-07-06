# Prime number generator using txt file with primes in already
# OPEN FILE WITH primes
import datetime
import sys

primes = []
sum = 0
infile = open("primes100.txt", 'r')
primes = infile.read().splitlines()
# using list comprehension to
# perform conversion
primes = [int(i) for i in primes]
for i in primes:
    sum += i
print(primes)
print("----------------")
print(sum)
print(primes[-1])
# Having imported prime list, use it to determine next prime
print("How many primes do you want?")
N = int(input())
begin_time = datetime.datetime.now()
print(N)
def CheckAgainstPrimesTxt(fN):
    if fN <= int(primes[-1]):
        print('We already calculated that prime'
        print(fN, 'is less than ', primes[-1])
        #stretch could be to calc and print nearest prime
        sys.exit()
#call function and check if we already have prime in list
CheckAgainstPrimesTxt(N)
print('carry on')
#use prime number list to test for primality
for a in primes


sys.exit()
while a < N:
    a =a+2
    j=3
    x=a
    while x > j:
        if x%j==0 and j!=x:
            #print x, " is not prime, divisible by ", j
            break
        j=j+2
    else:
        # print j,# " is prime, divisible by 1 and itself", x
        # primes.append(j)
        MyFile.write(str(j))
        MyFile.write('\n')
# print(primes)
# print(datetime.datetime.now() - begin_time)
#
# # MyFile=open('output.txt','w')
# # for element in primes:
# #      MyFile.write(str(element))
# #      MyFile.write('\n')
# # MyFile.close()
