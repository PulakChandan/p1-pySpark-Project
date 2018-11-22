#PF-Assgn-30
def encode():
    #Remove pass and write your logic here
    msg=input()+' '
    encoded_message=''
    count=1
    for i in range(0,len(msg)-1):
        if msg[i]==msg[i+1]:
            count+=1
        else:
            encoded_message+=str(count)+msg[i]
            count=1
           
    return encoded_message        
        
           
#Provide different values for message and test your program
encoded_message=encode()
print(encoded_message)