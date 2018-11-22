def check_palindrome(word):
    
    #Remove pass and write your logic here
    i=0
    j=len(word)-1
    for i in range(0,len(word)//2):
        if word[i]!=word[j]:
            return 0
        j-=1
    return 1
    
    
status=check_palindrome("malkalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
