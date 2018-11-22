import math
number=0
temp=number
sum_of_cubes=0
while number>0:
    sum_of_cubes+=pow(number%10,3)
    number//=10
if sum_of_cubes==temp:
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong number")
    