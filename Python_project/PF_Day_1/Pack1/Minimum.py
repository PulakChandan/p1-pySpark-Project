def minimum (n1,n2,n3):
    if n1< n2:
        if n1<n3:
            return n1
        else:
            return n2
    else:
        if n2<n3:
            return n2
        else:
            return n3
    
        

print(minimum(100,100,55))