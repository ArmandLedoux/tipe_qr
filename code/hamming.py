def hamming_decode(n, l) : 
    """l de taille 64"""
    q = l.copy()
    x = 0
    tot = 0
    for k in range (1, 1<<(2*n)):
        if l[k] == 1 :
            x = x ^ k
            tot = (tot + 1)
    if tot % 2 == l[0] and x != 0:
        print ("Au moins deux erreurs")
    else :
        q[x] = 1-q[x]
    return q

# tests hamming decode ----------------------------
# print([1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0])
# l = [0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0]
# print(l)
# print(hamming_decode(2, l))



def hamming_code (n,l) :
    """l de taille 64"""
    q = l.copy()
    x = 0
    tot = 0
    for k in range (1, 1<<(2*n)):
        if l[k] == 1 :
            x = x ^ k
            tot +=1 
    for i in range (2*n) :
        b = 1<<i
        q[b] = int(x&b != 0)
    q[0] = tot%2
    return q

# test hamming_code -------------------------------------------------
# l = [0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0]
# print(l)
# print(hamming_code(2,l))
