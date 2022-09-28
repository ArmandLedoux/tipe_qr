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

def hamming (lll) :
    """lll = [matrices de 64*64]
    On a lu les qr codes et formé nos paquets de 64 bits, 
    maintenant on corrige les potentielles erreurs et on retire les bits de parité."""
    pass

def lecture (lqr) : 
    """on a analysé l'image de qr code et rempli une liste du contenu du qr code, donc maint """
    iqr = 0 # numéro du qr code
    