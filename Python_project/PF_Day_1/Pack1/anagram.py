#PF-Assgn-54
def check_anagram(data1,data2):
    #start writing your code here
    str1=sorted(data1.lower())
    str2=sorted(data2.lower()) 
    if(str1 == str2):
        return True
    return False
      
print(check_anagram("integral","Triangle"))
