import numpy as np
def isol (l,n,k) :           #permet d'isoler un morceau du texte
    l2 = []
    for i in range (k) :
        if (i+n < len(l)):
             l2.append(l[i+n])  #on ajoute dans la liste qu'on utilise les éléments que l'ont veut manipuler
        else :
            l2.append(0)
    return l2

def faire_l (q,i,N=57) :
    '''l prends une liste et crée la liste de 57 éléments'''
    l1 = []
    for j in range (i,N+i) : 
        if (j < len(q)) :
            l1.append(q[j])      #si on est toujours dans le texte 
        else :
            l1.append(0)         #si on dépasse la fin du texte
    return l1

def faire_ll (q,i,n=64) :
    '''ll prend une liste q et crée un paquet de 57*64, donc 64 listes de 57 lettres'''
    ll = []                         
    for j in range (n) : 
        ll.append(faire_l(q,n*57*i+j*57))          #mets chaque l dans la ll chacun a son tour en faisant attention à ne pas prendre des éléments déjà présent dans une autre ll
    return ll


def faire_lll (q,N=57,n=64) : 
    """lll prend une liste q et crée une liste de toutes les ll de q"""       
    lll = []
    i = 0
    while(i*N*n<=len(q)) :       #agis tant qu'il est possible de créer une nouvelle ll avant la fin du texte 
        lll.append(faire_ll(q,i))  #insert toutes les ll dans lll 
        i += 1                   
    return lll

def print_list_list (lll) : 
    '''permet de mieux vérifier la correction de faire_lll'''
    for ll in lll :
        for l in ll :
            print (l)
        print(';')


# test = [i for i in range(72)]
# print_list_list(faire_lll (test))



def hamming_code (n,l) :
    """l de taille 64"""
    q = l.copy()
    x = 0
    tot = 0
    for k in range (1, 1<<(2*n)):   #concerne toutes les puissances de 2
        if l[k] == 1 :
            x = x ^ k               #applique le xor pour établir le nombre de 1
            tot +=1 
    for i in range (2*n) :
        b = 1<<i                    #remplie les bits de parité colonnes et lignes
        q[b] = int(x&b != 0)
    q[0] = tot%2                    #établi la valeur du bit de parité de la matrice positionné en 0
    return q

def l1_to_l2 (l,n) :
    '''copie une liste de taille n - le nb de bit de parité dans une liste de n en laissant les bits de parités vides'''
    q = [0]
    p = 1
    decal = 1
    for i in range (1,n):
        if i == p :
            q.append(0)
            p = p < 1
        else :
            q.append(l[i - decal])
    return q

# l = [1,1,1,1,1,1,1,1,1,1,1]
# print(l1_to_l2(l,16))

def faire_matrice_qr (n,l,inter) :
    m = np.zero(n,n)

    for i in range (7):
        m[0][i] = 1
        m[0][n-1-i] = 1
        m[6][i] = 1
        m[6][n-1-i] = 1
        m[n-1][i] = 1
        m[n-8][i] = 1
        m[i][0] = 1
        m[n-1-i][0] = 1
        m[i][6] = 1
        m[n-1-i][6] = 1
        m[i][n-1] = 1
        m[i][n-8] = 1
    
    for i in range (1,6):
        m[1][i] = 0
        m[1][n-1-i] = 0
        m[5][i] = 0
        m[5][n-1-i] = 0
        m[n-2][i] = 0
        m[n-6][i] = 0
        m[i][1] = 0
        m[i][5] = 0
        m[n-1-i][1] = 0
        m[n-1-i][5] = 0
        m[i][n-2] = 0
        m[i][n-6] = 0
       
    for i in range (2,4):
        m[2][i] = 1
        m[4][i] = 1
        m[2][n-1-i] = 1
        m[4][n-1-i]
        m[n-3][i] = 1
        m[n-5][i] = 1
        m[i][2] = 1
        m[i][4] = 1
        m[n-1-i][2] = 1
        m[n-1-i][4] = 1
        m[i][n-5] = 1
        m[i][n-3] = 1

    for k in range (len(l)):
        decal = 8
        i = k / n
        j = k % n

        if ((i > 7) or (j>7)) and ((i<n-8) or (j<n-8)) and ((i>7) or (j<n-8)):
            if ((i % inter == 4) or (i % inter == 8)):                      #horizontales des cercles les plus excentrés
                if (j % inter > 3) and (j % inter < 9):
                    m[i][j] = 1
            if (j % inter == 4) or (j % inter == 8):                        #verticales des cercles les plus excentrés
                if (j % inter > 3) and (j % inter < 9):
                    m[i][j] = 1
            if (i % inter > 4) or (i % inter < 8) :                         #horizonta les des cercles les moins excentrés
                if (j % inter > 4) and (j % inter < 8):
                    m[i][j] = 0
            if ( j % inter > 4) or (i % inter < 8) :                        #verticales des cercles les moins excentrés
                if (i % inter > 4) and (i % inter < 8):
                    m[i][j] = 0
            if (i % inter == 6) and (j % inter == 6):                       #petit carré du milieu
                m[i][j] = 1
