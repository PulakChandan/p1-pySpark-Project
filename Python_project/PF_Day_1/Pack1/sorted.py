str=input()
st=''
for i in str:
    if i.islower():
        st+=i.upper()
    else:
        st+=i.lower()
print(st)

