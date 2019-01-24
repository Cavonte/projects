def isInterleaving(s1,s2,s3):
    if len(s3) != len(s1) + len(s2):
        return False
    cs1 = 0
    cs2 = 0
    cs3 = 0
    while cs3 < len(s3):
        localCS1 = cs1
        localCS2 = cs2
        localCS3 = cs3
        while localCS1 < len(s1) and localCS3 < len(s3) and s3[localCS3] == s1[localCS1]:
            localCS1 = localCS1 + 1
            localCS3 = localCS3 + 1
            print(s3[localCS1],'1')
        localCS3 = cs3
        while localCS2 < len(s2) and localCS3 < len(s3) and s3[localCS3] == s2[localCS2]:
            localCS2 = localCS2 + 1
            localCS3 = localCS3 + 1
            print(s3[localCS2],'2')
        if localCS2 > localCS1:
            cs2 = cs2 + localCS2
        else:
            cs1 = cs1 + localCS1

        cs3 = cs3 + localCS3

    if cs1 == len(s1) and cs2 == len(s2):
        return True
    return False


"aabc"
"abad"
"aabadabc"

"aabcc"
"dbbca"
"aadbbcbcac"

sent1 = "aabcc"
sent2 = "dbbca"
print(isInterleaving(sent1,sent2,"aadbbcbcac"))



