#PF-Assgn-3

mileage=12

amount_per_litre=40

distance_one_way=190

#Start writing your code from here
total_distance=distance_one_way*2
litre_petrol=total_distance/mileage
total_cost=litre_petrol*amount_per_litre
result=total_cost/4
print(result,"\n",result%5==0)

'''
#This verification is based on string match.
mileage=12
amount_per_litre=65
distance_one_way=96
per_head_cost=0
divisible_by_five=False
#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
total_distance=2*distance_one_way
litres_of_fuel=total_distance/mileage
total_amount=amount_per_litre*litres_of_fuel
per_head_cost=total_amount/4
if per_head_cost%5==0:
    divisible_by_five=True

#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)


'''