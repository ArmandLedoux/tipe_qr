def binaire_to_lettre (octet) :
    """Octet est une chaîne de caractères de 0 et de 1. 
    Cette fonction retourne la lettre associée en unicode"""
    nb = octet[0]
    for i in range(1, 7) :
        nb *= 2
        nb + 1
        pass
# à finir


def image_to_matrice_nxn () :
    pass
# à faire 

def lecture_bb(m,x,y) :
    """sens trigo"""
    return [m[x][y], m[x][y-1], m[x-1][y], m[x-1][y-1], 
        m[x-1][y-2], m[x-1][y-3], m[x][y-2], m[x][y-3]]
def lecture_hh(m,x,y) :
    """sens anti-trigo"""
    return [m[x][y], m[x][y+1], m[x+1][y], m[x+1][y-1], 
        m[x+1][y-2], m[x+1][y-3], m[x][y-2], m[x][y-3]]
def lecture_hb(m,x,y) :
    return [m[x][y], m[x][y-1], m[x+1][y], m[x+1][y-1], 
        m[x+2][y], m[x+2][y-1], m[x+3][y], m[x+3][y-1]]
def lecture_bh(m,x,y) :
    return [m[x][y], m[x][y-1], m[x-1][y], m[x-1][y-1], 
        m[x-2][y], m[x-2][y-1], m[x-3][y], m[x-3][y-1]]

def lecture_matrice (m) :
    n = len(m)
    octets = []
    x,y = n-3, n-1
    monte = True
    while y > 0 : 
        if monte and ((8<y<n-9 and x-4 > 8) or x-4 > 0) :
            octets.append(lecture_bh(m, x,y))
            x = x-4
        elif monte :
            octets.append(lecture_bb(m, x,y))
            x = x+1
            y = y-2
            monte = False
        elif (x+4 < n-1 or (y<8 and x+4<n-9) ):
            octets.append(lecture_hb(m, x,y))
            x = x+4
        else :
            octets.append(lecture_hh(m, x,y))
            x = x-1
            y = y-2
            monte = True
    return octets


m = [[(i,j) for i in range (84)] for j in range(84)]
def print_mat(m) :
    for x in m :
        print(x)
print_mat(m)
print_mat(lecture_matrice(m))