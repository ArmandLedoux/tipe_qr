def concat (l1, l2) :
    for i in l2 :
        l1.append(i)
def assemble(lll) :
    """lll = [matrices de 64*57]
    Hamming a corrigé les erreurs et retiré les bits de parité, maintenant on recompose la liste de bits."""
    sequence = []
    for ll in lll :
        for l in ll :
            concat(sequence, l)
    return sequence

# -------------------------------------------------------------------------------------
# tests assemble

# lll = [[[i+l*20+100*j for i in range(20)] for l in range(5)] for j in range (8)]

# def print_list_list (lll) : 
#     for ll in lll :
#         for l in ll :
#             print (l)
#         print(';')
# -------------------------------------------------------------------------------------
assemble()

def application_hamming (lll) :
    """lll = [matrices de 64*64]
    On a lu les qr codes et formé nos paquets de 64 bits, 
    maintenant on corrige les potentielles erreurs"""
    def hamming_decode(l, n=3) : # on code dans le cas général
        x = 0
        tot = 0
        for k in range (1, 1<<(2*n)):
            if l[k] == 1 :
                x = x ^ k
                tot = (tot + 1)
        if tot % 2 == l[0] and x != 0:
            print ("Au moins deux erreurs")
        else :
            l[x] = 1-l[x]
    for ll in lll :
        for l in ll :
            hamming_decode(l)
    
    
def retire_bits_de_parite(l) :
    """on a corrigé les erreurs, donc on peut retirer les bits de parité"""
    q = []
    puiss2 = 1
    for i in range (1,len(l)) :
        if i == puiss2 : # les bits de parité sont des puissances de 2
            puiss2 = puiss2<<1
        else :
            q.append(l[i])
    return q

# tests retire -----------------------
# l = [randint(0,1) for i in range(16)]
# print(l)
# print(retire_bits_de_parite(l))



def lecture (lqr) : 
    """on a analysé l'image de qr code et rempli une liste du contenu du qr code, donc maint """
    iqr = 0 # numéro du qr code
    