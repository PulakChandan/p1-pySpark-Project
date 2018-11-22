list=[1,3,5,6]
even=0
swap=0
for i in list:
    if i%2==0:
        even+=1
for i in range(0,even):
    if list[i]%2!=0:
        swap+=1  
print(swap)
        

    