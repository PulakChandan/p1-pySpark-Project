from nt import fstat
def sec_max(numList):
    numList.sort(reverse=True)
    return numList[1]

def sec_max1(numList):
    fst=numList[0]
    sec=numList[0]
    for i in range(1,len(numList)):
        if numList[i] > sec and numList[i] > fst:
            sec=fst
            fst=numList[i]
        elif numList[i]>sec and numList[i]<fst:
            sec=numList[i]
    return sec        
        

numList=[34,12,78,3,0,19,3,13,5]
print(sec_max1(numList))