#factorial
facto=1   #global
def fact(num):
    if num==0:
        return 1
    else:
        if num >0:
            global facto
            facto*=num 
            fact(num-1)
            
        return facto
            





n=6
print("Factorial of",n,":",fact(n))