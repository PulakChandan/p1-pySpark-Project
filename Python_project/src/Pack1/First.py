# Get L and R from the input
#def raw_input():
#    return "2 5";
L, R = map(int, input().split())

# Write here the logic to print all integers between L and R
for i in range(L,R+1):
    print(i, end=" ");

