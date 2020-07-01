import datetime
print("How many primes do you want?")
N = input()
begin_time = datetime.datetime.now()
a = 3
primes = [2,3]
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
        #print j,# " is prime, divisible by 1 and itself", x
        primes.append(j)
print(primes)
print(datetime.datetime.now() - begin_time)

MyFile=open('output.txt','w')

for element in primes:
     MyFile.write(str(element))
     MyFile.write('\n')
MyFile.close()
