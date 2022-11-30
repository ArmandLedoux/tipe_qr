def faire_lll (texte, nb_mat, nb_cor) : 
    """faire_lll prend une liste texte et crée une liste de toutes les paquets de texte"""
    texte.append(1)
    n = (1<<nb_cor) - nb_cor -1
    lll = []
    i = 0
    while(i<=len(texte)) : # pour chaque paquet 
        lll.append(faire_ll(texte,i,nb_mat,n))  #insert toutes les ll dans lll 
        i += nb_mat*n   
    texte.pop()               
    return lll

def faire_ll (texte,i,nb_mat, n) :
    '''ll prend une liste texte et crée un paquet de 57*64, donc 64 listes de 57 lettres'''
    ll = []                         
    for j in range (nb_mat) : 
        ll.append(faire_l(texte,i+j*57,n))          #mets chaque l dans la ll chacun a son tour en faisant attention à ne pas prendre des éléments déjà présent dans une autre ll
    return ll

def faire_l (texte,i,n) :
    '''l prends une liste et crée la liste de 57 éléments'''
    l1 = []
    for j in range (i,n+i) : 
        if (j < len(texte)) :
            l1.append(texte[j])      #si on est toujours dans le texte 
        else :
            l1.append(0)         #si on dépasse la fin du texte
    return l1






# def print_list_list (lll) : 
#     '''permet de mieux vérifier la correction de faire_lll'''
#     for ll in lll :
#         for l in ll :
#             print (l)
#         print(';')


def ajoute_bits_de_parite (l,nb_cor) :
    '''copie une liste de taille n moins le nb de bit de parité dans une liste de n en laissant les bits de parités vides'''
    n = 1<<nb_cor
    q = [0]
    p = 1 # puissances de deux, indices des bits de parite
    decal = 1 # combien de bits de parité on a ajouté
    for i in range (1,n):
        if i == p :
            q.append(0)
            p = p << 1
            decal += 1
        else :
            q.append(l[i - decal])
    return q


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
        b = 1<<i                    #remplie les bits de parité colonnes et lignes
        q[b] = int(x&b != 0)
    q[0] = tot%2                    #établi la valeur du bit de parité de la matrice positionné en 0
    return q


def recompose (lll) : 
    """recompose prend la liste des paquets de matrices de correction, 
    et renvoie une liste de bits en répartissant chaque matrice de cor au sein du paquet"""
    sequence = []
    for ll in lll : 
        for j in range(len(ll[0])) :
            for i in range(len(ll)) :
                sequence.append(ll[i][j])
    return sequence



def faire_matrice_qr (n) :
    '''fonction longue et moche qui crée un qr code qui condient les carrés dans les coins
    -1 = vide '''
    m = []
    for i in range (n):
        m.append([])
        for j in range (n):
            m[i].append(-1)
    
    for i in range (8):
        m[7][i] = 1
        m[7][n-1-i] = 1
        m[i][7] = 1
        m[n-1-i][7] = 1
        m[n-8][i] = 1
        m[i][n-8] = 1

    for i in range (7):
        m[0][i] = 0
        m[0][n-1-i] = 0
        m[6][i] = 0
        m[6][n-1-i] = 0
        m[n-1][i] = 0
        m[n-7][i] = 0
        m[i][0] = 0
        m[n-1-i][0] = 0
        m[i][6] = 0
        m[n-1-i][6] = 0
        m[i][n-1] = 0
        m[i][n-7] = 0
    
    for i in range (1,6):
        m[1][i] = 1
        m[1][n-1-i] = 1
        m[5][i] = 1
        m[5][n-1-i] = 1
        m[n-2][i] = 1
        m[n-6][i] = 1
        m[i][1] = 1
        m[i][5] = 1
        m[n-1-i][1] = 1
        m[n-1-i][5] = 1
        m[i][n-2] = 1
        m[i][n-6] = 1
       
    for i in range (2,5):
        m[2][i] = 0
        m[4][i] = 0
        m[2][n-1-i] = 0
        m[4][n-1-i] = 0
        m[n-3][i] = 0
        m[n-5][i] = 0
        m[i][2] = 0
        m[i][4] = 0
        m[n-1-i][2] = 0
        m[n-1-i][4] = 0
        m[i][n-5] = 0
        m[i][n-3] = 0
    
    m[3][3] = 0
    m[3][n-4] = 0
    m[n-4][3] = 0

    # for i in range (n):
    #     for j in range (n) :
    #         if (m[i][j] == -1):
    #             if ((i % inter == 4) or (i % inter == 8)):                      #horizontales des cercles les plus excentrés
    #                 if (j % inter > 3) and (j % inter < 9):
    #                     m[i][j] = 1
    #             if (j % inter == 4) or (j % inter == 8):                        #verticales des cercles les plus excentrés
    #                 if (i % inter > 3) and (i % inter < 9):
    #                     m[i][j] = 1
    #             if (i % inter > 4) and (i % inter < 8) :                         #horizonta les des cercles les moins excentrés
    #                 if (j % inter > 4) and (j % inter < 8):
    #                     m[i][j] = 0
    #             if ( j % inter > 4) and (j % inter < 8) :                        #verticales des cercles les moins excentrés
    #                 if (i % inter > 4) and (i % inter < 8):
    #                     m[i][j] = 0
    #             if (i % inter == 6) and (j % inter == 6):                       #petit carré du milieu
    #                 m[i][j] = 1
    return m



            


def remplir_lqr (l, largeur=64):
    '''rempli le qr code après l'implémentation de chaque petits et grands carrés
    n est la largeur du qr code'''
    m = len(l)
    lqr = []
    i = 0 # i va de 0 à m
    while i<m : # un passage par qr code
        mat = faire_matrice_qr(largeur)
        for x in range(largeur) :
            for y in range(largeur) :
                if mat[x][y] == -1 :
                    if i==m :
                        mat[x][y] = 0
                    else :
                        mat[x][y] = l[i]
                        i = i+1
        lqr.append(mat)
    return lqr
                



# def print_qr (qr) : 
#     '''permet de mieux vérifier la correction de faire_qr'''
#     for i in range(len(qr)) :
#         line = ""
#         for j in range(len(qr)) :
#             if qr[i][j] == 0 :
#                 line = line+ '¤'
#             elif qr[i][j] == -1 :
#                 line = line + '-'
#             elif qr[i][j] == 1 :
#                 line = line + '*'
#             else :
#                 line = line + str(qr[i][j])
#         print(line)




def encodage (texte, nb_mat=64, nb_cor=3) : 
    '''nb_mat : taille des matrices de correction d'erreur 
    nb_cor + 1 : nombre de bits de correction d'erreur par matrices de correction d'erreur
    2^nb_cor = taille des matrices de correction d'erreur'''
    lll = faire_lll(texte, nb_mat, nb_cor)
    for paquet in range(len(lll)) : 
        for mat_cor in range(len(lll[paquet]))  :
            lll[paquet][mat_cor] = ajoute_bits_de_parite(lll[paquet][mat_cor], nb_cor)
            lll[paquet][mat_cor] = hamming_code (lll[paquet][mat_cor], nb_cor)
    l = recompose(lll)
    lqr = remplir_lqr(l)

    return lqr

# texte = [randint(0,1) for i in range(10000)]
# print(encodage(texte))
