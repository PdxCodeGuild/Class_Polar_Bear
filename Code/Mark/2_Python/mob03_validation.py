

def cc_valid(ccn):
    s = list(map(int,(ccn[:-1])))
    s = s[::-1]

    for i in range(0,len(s),2):
        s[i] = 2 * s[i]
        
    for i in range(len(s)):
        if s[i] > 9:
            s[i] -= 9

    x = sum(s)
    c = str(x)[1]
    return c == ccn[-1]
    

print(cc_valid('4556737586899855'))
