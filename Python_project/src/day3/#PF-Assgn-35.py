#PF-Assgn-35
#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    #Remove pass and write your logic here
    average_mark=sum(list_of_marks)//len(list_of_marks)
    count=0
    for mark in list_of_marks:
        if mark>average_mark:
            count+=1
    return (count/len(list_of_marks))*100
            
            

def sort_marks():
    
    #Remove pass and write your logic here
    temp=list(list_of_marks)
    temp.sort()
    return temp

def generate_frequency():
    #Remove pass and write your logic here
    freq_list=[0]*(max(list_of_marks)+1)
    for i in range(0,len(freq_list)):
        freq_list[i]=list_of_marks.count(i)
    return freq_list

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())



