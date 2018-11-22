str=input();
ans='';
for ltr in str:
    if ltr.islower():
        ans+=ltr.upper()
    else:
        ans+=ltr.lower()
print(ans);

'''import sys;
str=(sys.stdin.readline());
print(str.swapcase());
'''
