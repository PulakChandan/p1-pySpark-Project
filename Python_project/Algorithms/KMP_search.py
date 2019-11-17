def findLPS(pat):
    M = len(pat)
    fail = [0] * M
    fail[0] = 0
    i = 0
    j = 1
    while j < M:
        print(fail, i, j)
        if pat[i] == pat[j]:
            fail[j] = i + 1
            i, j = i + 1, j + 1
        else:
            if i != 0:
                i = fail[i - 1]
            else:
                fail[j] = fail[i]
                j += 1
    return fail


def KMP_search(str, pattern):
    N = len(str)
    M = len(pattern)
    fail = findLPS(pattern)
    print(fail)
    j = 0
    i = 0
    while i < N:
        if pattern[j] == str[i]:
            j+=1
            i+=1
        if j == M:
            print "Pattern found at pos:", (i-M)
            j = fail[j-1]

        #mismatch after j matches
        elif i < N and pattern[j] != str[i]:
            if j != 0:
                j = fail[j-1]
            else:
                i+=1

pattern = 'ABAB'
str = 'ABABDABAABAACDABABCAABAACAAABABABAACAABAAB'
KMP_search(str, pattern)




