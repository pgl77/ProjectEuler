# Prime number generator using txt file with primes in already
# OPEN FILE WITH primes
primes = []
lines = open("primes100.txt").readlines()
for line in lines:
    primes(line) = int(lines(line))

print(primes)

# MyFile=open('output.txt','w')
# MyFile.write("2")
# MyFile.write('\n')
# MyFile.write("3")
# MyFile.write('\n')
# import datetime
# print("How many primes do you want?")
# N = input()
# begin_time = datetime.datetime.now()
# a = 3
# primes = [2,3]
# while a < N:
#     a =a+2
#     j=3
#     x=a
#     while x > j:
#         if x%j==0 and j!=x:
#             #print x, " is not prime, divisible by ", j
#             break
#         j=j+2
#     else:
#         # print j,# " is prime, divisible by 1 and itself", x
#         # primes.append(j)
#         MyFile.write(str(j))
#         MyFile.write('\n')
# # print(primes)
# print(datetime.datetime.now() - begin_time)
#
# # MyFile=open('output.txt','w')
# # for element in primes:
# #      MyFile.write(str(element))
# #      MyFile.write('\n')
# # MyFile.close()
