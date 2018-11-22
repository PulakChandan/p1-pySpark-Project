from operator import itemgetter
N,M=map(int,input().split())
f_list=[]
for i in range(0,N):
    t_list=list(map(int,input().split()))
    f_list.append(t_list)    
k=int(input())
f_list.sort(key=itemgetter(int(k)))
#f_list.sort(key=lambda x,k:x[k])
        
print(f_list)
print("10"+20)