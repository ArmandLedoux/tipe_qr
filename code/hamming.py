def hamming_decode(l, nb_cor) : 
    """D'après hamming, l'erreur, si elle existe et si elle est seule,
    se trouve aux coordonnées fournies par le xor de tous les bits impairs
    (les bits de parités sont là pour s'assurer ce résultat,
    via une méthode dichotomique sur les lignes et les colonnes)"""
    xor = 0
    tot = 0
    for k in range (1, 1<<(nb_cor)):
        if l[k] == 1 :
            xor = xor ^ k
            tot += 1
    if tot % 2 == l[0] and xor != 0:
        # print ("Au moins deux erreurs")
        pass
    else :
        l[xor] = 1-l[xor]

def hamming_code (l,nb_cor=6) :
    """l de taille 64"""
    q = l.copy()
    x = 0
    tot = 0
    for k in range (1, 1<<(nb_cor)):   #concerne toutes les puissances de 2
        if l[k] == 1 :
            x = x ^ k               #applique le xor pour établir le nombre de 1
            tot +=1 
    for i in range (nb_cor) :
        b = 1<<i                    #représente chacun des bits
        q[b] = int(x&b != 0)
    q[0] = tot%2                    #établis la valeur du bit de parité de la matrice positionné en 0
    return q