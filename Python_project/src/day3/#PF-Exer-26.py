#PF-Exer-26
def factorial(number):
    #remove pass and write your logic to find and return the factorial of given number
    if number==0:
        return 1
    else:
        fact=1
        while number>0:
            fact*=number
            number-=1
        return fact
        

def find_strong_numbers(num_list):
    #remove pass and write your logic to find and return the list of strong numbers from the given list
    strong_num_list=[]
    for num in num_list:
        temp=num 
        sum_fact=0
        while temp>0:
            sum_fact+=factorial(temp%10)
            temp//=10
        if sum_fact == num:
            strong_num_list.append(num)
    return strong_num_list
num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
