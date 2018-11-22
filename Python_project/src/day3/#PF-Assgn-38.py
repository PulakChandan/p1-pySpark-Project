num=125874
doub=num*2
st1=str(125874)
list1=[]
list2=[]
if(len(str(num))!=len(str(doub))):
    print("False")
    exit(0)
else:
    while num>0:
        list1.append(num%10)
        list2.append(doub%10)
        num//=10
        doub//=10
for number in list1:
    if number not in list2:
        print("False")
        exit(0)
print("True")
           





