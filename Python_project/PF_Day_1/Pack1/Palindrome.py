value=167557612
temp_value=value
reverse_value=0
while value>0:
    reverse_value=reverse_value*10+(value%10)
    value//=10
print(reverse_value)
if temp_value==reverse_value:
    print(temp_value,"is palindrome")
else:
    print(temp_value,"is not palindrome")