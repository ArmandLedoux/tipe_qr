def zone_a_lire (x, y, n) :
    if x < 8 and y < 8 :
        return False
    elif x < 8 and y >n-9 :
        return False
    elif x > n-9 and y<8 :
        return False
    else : 
        return True

def lecture_matrice (llqr) :
    taille_qr = len(llqr[0])
    lqr = []
    for iqr in range(len(llqr)) :
        qr = []
        for x in range(taille_qr) :
            for y in range(taille_qr) :
                if zone_a_lire(x,y,taille_qr) :
                    qr.append(llqr[iqr][x][y])
        lqr.append(qr)
    return lqr

def formation_des_paquets (lqr, nb_mat, nb_cor) : 
    """après lecture du qr code, on a créé une liste contenant chacun des qr codes sous forme de listes.
    on les convertit en une liste de paquets contenant nb_mat matrices de correction d'erreur,
    chacune comprenant nb_cor+1 bits de correction d'erreur (soit de taille 1<<nb_cor)"""
    n = 1<<nb_cor
    lpaquet = [] # liste des paquets
    paquet = [] # contient un paquet de taille n*nb_mat
    i = 0 # pour repérer où on est dans le paquet
    for qr in lqr :
        for j in range(len(qr)) :
            paquet.append(qr[j])
            i+=1
            if i == nb_mat*n : # on a terminé un paquet
                i = 0
                lpaquet.append(paquet) 
                paquet = []
    lll = [formation(paquet,nb_mat,n) for paquet in lpaquet]
    return lll 

def formation (paquet, nb_mat, n) :
    """prépare les paquets de matrices de correction d'erreur pour hamming"""
    ll = []
    for i in range (nb_mat) :
        l = []
        for j in range(n) :
            l.append(paquet[j*n+i])
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




def correction_d_erreur (lll, nb_cor) :
    """lll = [matrices de 64*64]
    On a lu les qr codes et formé nos paquets de 64 bits, 
    maintenant on corrige les potentielles erreurs"""

    def hamming_decode(l, nb_cor) : # on code pour une taille générale au cas où l'efficacité d'une matrice 8x8 serait mauvaise
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
    for ll in lll :
        for l in ll :
            hamming_decode(l, nb_cor)
    


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
    """lll = [matrices de 64*64]
    Hamming a corrigé les erreurs, maintenant on retire les bits de parité recompose la liste de bits."""
    for a in range(len(lll)) :
        ll = lll[a]
        for b in range(len(ll)) :
            ll[b] = retire_bits_de_parite(ll[b])
    
    def concat (l1, l2) :
        for i in l2 :
            l1.append(i)
    sequence = []
    for ll in lll :
        for l in ll :
            concat(sequence, l)
    # return sequence
    n = len(sequence) 
    # temp = ""
    # for i in range(n) :
    #     temp+=str(sequence[i])
    # print(temp, ";")
    # print("-------------------------------------------")
    compteur = 0
    # temp = ''
    for i in range(n-1,-1,-1) :
        compteur +=1
        if sequence[i] != 0 :
            # for j in range (i-50, i+50) :
            #     temp+=str(sequence[j])
            # print(temp)
            return sequence[:i]
        
    

# -------------------------------------------------------------------------------------
# tests assemble

# lll = [[[i+l*20+100*j for i in range(20)] for l in range(5)] for j in range (8)]

# def print_list_list (lll) : 
#     for ll in lll :
#         for l in ll :
#             print (l)
#         print(';')
# -------------------------------------------------------------------------------------



def decodage (llqr,nb_mat=64,nb_cor=6) :
    lqr = lecture_matrice(llqr)
    lll = formation_des_paquets (lqr, nb_mat, nb_cor)
    correction_d_erreur (lll,nb_cor)
    return assemble(lll)


# llqr = [[[randint(0,1) for i in range(64)] for j in range(64)] for i in range(5)]

# print(decodage(llqr))

# print("ok")


#SCANNER LE QR CODE VIDEO 

import cv2

# Ouverture de la vidéo
video = cv2.VideoCapture('ma_video.mp4')

# Boucle pour extraire chaque image
success, image = video.read()
count = 0
while success:
    # Enregistrement de l'image extraite
    cv2.imwrite("frame%d.jpg" % count, image)
    success, image = video.read()
    count += 1

#ensuite il faut que j'implémente une fonction qui prends une vidéo filmé par un téléphone et qui traduit les qr codes etc...

from pyzbar.pyzbar import decode
from PIL import Image

def qr_code_to_text(image_path):
    # Ouvrir l'image contenant le code QR
    image = Image.open(image_path)

    # Décoder le code QR
    qr_codes = decode(image)

    # Extraire le texte du code QR
    text = ''
    for qr_code in qr_codes:
        text += qr_code.data.decode('utf-8')

    return text

# Chemin d'accès à l'image contenant le code QR
image_path = 'chemin/vers/qr_code.png'

# Appeler la fonction pour traduire le code QR en texte
qr_text = qr_code_to_text(image_path)

# Afficher le texte extrait du code QR
print("Code QR traduit en texte :", qr_text)
