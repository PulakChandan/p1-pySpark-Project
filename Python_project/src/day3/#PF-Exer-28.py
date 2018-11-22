#PF-Exer-28
from collections import Counter                                            
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    count=Counter(match_tuple)
    max_list=[]
    for key,value in count.items():
        if value==max(count.values()):    #prints multiple keys with max values
            max_list.append(key)
    print(max_list)
    if len(max_list)==1:
        return max_list[0]
    else:
        return 'Tie'
#Invoke the function with each of the print statements given below
#print(find_winner_of_the_day("Team1","Team2","Team1"))
print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))

