import math
N=input()
lis=list(map(int,input().split()))
prod=1
for i in lis:
    prod=(prod*i)%(pow(10,9)+7)
print(prod)