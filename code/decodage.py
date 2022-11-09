def formation_des_paquets (lqr, N=64, n=64) : 
    """après lecture du qr code, on a créé une liste contenant chacun des qr codes sous forme de listes.
    on les convertit en une liste de paquets contenant N grilles à n élements pour hamming"""
    llpaquet = [] # liste des paquets
    lpaquet = [] # contient un paquet de taille 64*64 = 4096
    i = 0 # pour repérer où on est dans le paquet
    for qr in lqr :
        for j in range(len(qr)) :
            lpaquet.append(qr[j])
            i+=1
            if i == n*N : # on a terminé un paquet
                i = 0
                llpaquet.append(lpaquet) 
                lpaquet = []
    lll = [formation(lpaquet,N,n) for lpaquet in llpaquet]
    return lll 
    # si on a un lpaquet non vide à la fin de l'algo, c'est qu'on a créé un début de lpaquet pour remplir le dernier qr code

def formation (lpaquet, N, n) :
    ll = []
    for i in range (N) :
        l = []
        for j in range(n) :
            l.append(lpaquet[j*64+i])
        ll.append(l)
    return ll


# -------------------------------------------------------------------------------------
# tests formation_des_paquets

# def print_list_list (lll) : 
#     for ll in lll :
#         for l in ll :
#             print (l)
#         print(';')

# l = [[i*1000 + j for j in range(1000)]for i in range(9)]
# q = formation_des_paquets(l)

# print_list_list (q)
# print(len(q), len(q[0]),len(q[0][0]))
# -------------------------------------------------------------------------------------




def correction_d_erreur (lll) :
    """lll = [matrices de 64*64]
    On a lu les qr codes et formé nos paquets de 64 bits, 
    maintenant on corrige les potentielles erreurs"""

    def hamming_decode(l, n=3) : # on code pour une taille générale au cas où l'efficacité d'une matrice 8x8 serait mauvaise
        """D'après hamming, l'erreur, si elle existe et si elle est seule,
        se trouve aux coordonnées fournies par le xor de tous les bits impairs
        (les bits de parités sont là pour s'assurer ce résultat,
        via une méthode dichotomique sur les lignes et les colonnes)"""
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

# -------------------------------------------------------------------------------------
# tests retire_bits_de_parite 

# l = [randint(0,1) for i in range(16)]

# print(l)
# print(retire_bits_de_parite(l))
# -------------------------------------------------------------------------------------




def assemble(lll) :
    """lll = [matrices de 64*57]
    Hamming a corrigé les erreurs et retiré les bits de parité, maintenant on recompose la liste de bits."""
    def concat (l1, l2) :
        for i in l2 :
            l1.append(i)
    sequence = []
    for ll in lll :
        for l in ll :
            concat(sequence, l)
    return sequence
    n = len(sequence) 
    for i in range(n-1,-1,-1) :
        if sequence[i] != 0 :
            return sequence[:i-1]
        
    

# -------------------------------------------------------------------------------------
# tests assemble

# lll = [[[i+l*20+100*j for i in range(20)] for l in range(5)] for j in range (8)]

# def print_list_list (lll) : 
#     for ll in lll :
#         for l in ll :
#             print (l)
#         print(';')
# -------------------------------------------------------------------------------------


