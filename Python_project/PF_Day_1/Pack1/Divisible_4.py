sum=0
while 1:
    print("Enter the number(0 to end):")
    number=int(input())
    if number==0:
        break
    elif number%4==0:
        sum+=number
print("Sum of numbers divisible by 4 is:",sum)
    