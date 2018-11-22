st1="I like Python"
st2="Java is a very popular language"
result_string=''
for ltr in st1:
    if ltr in st2 and ltr!=' ':
        result_string+=ltr
print(result_string)
# in alpgabetical order
alp_list=[]
for i in result_string:
    alp_list.append(i)    
alp_list.sort()
result_string=''
for i in alp_list:
    result_string+=i
print(result_string)
   
    
    