#Largest prime factor
#Problem 3 
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Range to test for primality - start with 3 and step in 2 (all prime numbers after 2 odd)
import math
ceiling = 20
formatter = "%r %r "
primes=[2,3]
for i in range(3, ceiling, 2):
    print("---------------------------")
    j = int(math.ceil(i**.5))
    for x in range (j,2,-1):
        print formatter % (i, j)
        if i%j == 0:
            print ("Not prime")
            break
        #elif:
        else: 
            print ("Prime")
            primes.append(i)  
    print("---------------------------")
print primes
    
    
