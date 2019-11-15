def findLPS(pat):
    M = len(pat)
    fail = [0] * M
    fail[0] = 0
    i=0
    for j in range (1, M):
        if pat[i] == pat[j]:
            fail[j] = i+1
            i+=1
        else:
            if i !=0:
                i-=1
            fail[j] = fail[i]
            i = 0
    return fail


def KMP_search(str, pattern):
    N = len(str)
    M = len(pattern)
    fail = findLPS(pattern)
    j = 0
    i = 0
    while i < N:
        if pattern[j] == str[i]:
            j+=1
            i+=1
        if j == M:
            print("Pattern found at pos:" + str(i-M))
            j = fail[j-1]

        #mismatch after j matches
        elif i < N and pattern[j] != str[i]:
            if j != 0:
                j = fail[j-1]
            else:
                i+=1

pattern = 'ABABCABAB'
str = 'ABABDABACDABABCABAB'
KMP_search(pattern, str)




