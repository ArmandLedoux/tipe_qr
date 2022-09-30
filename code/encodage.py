def isol (l,n,k) :           #permet d'isoler un morceau du texte
    l2 = []
    for i in range (k) :
        if (i+n < len(l)):
             l2.append(l[i+n])
        else :
            l2.append(0)
    return l2

def faire_l (q,i) :
    '''l prends une liste et crée la liste de 57 éléments'''
    l1 = []
    for j in range (i,57+i) : 
        if (j < len(q)) :
            l1.append(q[j])      #si on est toujours dans le texte 
        else :
            l1.append(0)         #si on dépasse la fin du texte
    return l1

def faire_ll (q,i) :
    '''ll prend une liste q et crée un paquet de 57*64, donc 64 listes de 57 lettres'''
    ll = []                         
    for j in range (64) : 
        ll.append(faire_l(q,64*57*i+j*57))          #mets chaque l dans la ll chacun a son tour
    return ll


def faire_lll (q) : 
    """lll prend une liste q et crée une liste de toutes les ll de q"""       
    lll = []
    i = 0
    while(i*57*64<=len(q)) :
        lll.append(faire_ll(q,i))  #insert toutes les ll dans lll 
        i += 1                   
    return lll

def print_list_list (lll) : 
    for ll in lll :
        for l in ll :
            print (l)
        print(';')


test = [i for i in range(7297)]
print_list_list(faire_lll (test))




# def hamming_code (n,l) :
#     """l de taille 64"""
#     q = l.copy()
#     x = 0
#     tot = 0
#     for k in range (1, 1<<(2*n)):
#         if l[k] == 1 :
#             x = x ^ k
#             tot +=1 
#     for i in range (2*n) :
#         b = 1<<i
#         q[b] = int(x&b != 0)
#     q[0] = tot%2
#     return q

# def l1_to_l2 (l,n) :
#     '''copie une liste de taille n - le nb de bit de parité dans une liste de n en laissant les bits de parités vides'''
#     q = [0]
#     p = 1
#     decal = 1
#     for i in range (1,n):
#         if i == p :
#             q.append(0)
#             p = p << 1
#             decal += 1
#         else :
#             q.append(l[i - decal])
#     return q

# l = [1,1,1,1,1,1,1,1,1,1,1]
# print(l1_to_l2(l,16))