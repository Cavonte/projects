def isInterleaving(s1,s2,s3):
    if len(s3) != len(s1) + len(s2):
        return False
    cs1 = 0
    cs2 = 0
    cs3 = 0
    while cs3 < len(s3):
        while cs1 < len(s1)  and s3[cs3] == s1[cs1]:
            cs1 = cs1 + 1
            cs3 = cs3 + 1
            print("s11")
        while cs2 < len(s2) and s3[cs3] == s2[cs2]:
            cs2 = cs2 + 1
            print("s22")
            cs3 = cs3 + 1
        cs3 = cs3 + 1

    if cs3 < len(s3):
        return False
    return True


"aabc"
"abad"
"aabadabc"

sent1 = "a"
sent2 = "abad"
print(isInterleaving(sent1,sent2,"aabadabc"))



