#PF-Assgn-30
from collections import Counter
def max_speciality(patient_list,speciality_dict):
    #Remove pass and write your logic here
    buffer_list=[]
    for i in range(1,len(patient_list),2):
        buffer_list.append(patient_list[i])
    count=Counter(buffer_list)
    print(count);
    max_spec=max(count,key=count.get)    
    print(max_spec)
    for key,value in speciality_dict.items():
        if key==max_spec:
            return value
           
#Provide different values for message and test your program
patient_list=[405,'P',102,'P',609,'E',101,'E',900,'O',430,'E']
speciality_dict={'P':'Pediatrics','E':'ENT','O':'Orthopaedics'}
print(max_speciality(patient_list,speciality_dict))