def isol (l,n,k) :           #permet d'isoler un morceau du texte
    l2 = []
    for i in range (k) :
        l2.append(l[i+n])
    return l2

def faire_l (q,i) :
    '''l prends une liste et crée la liste de 57 éléments'''
    l1 = []
    for j in range (57) : 
        if (i + j < len(q)) :
            l1.append(q[i +j])      #si on est toujours dans le texte 
        else :
            l1.append(0)         #si on dépasse la fin du texte
    return l1

def faire_ll (q) :
    '''ll prend une liste q et crée un paquet de 57*64, donc 64 listes de 57 lettres'''
    ll = []                         
    for i in range (64) : 
        ll.append(faire_l(q,i))          #mets chaque l dans la ll chacun a son tour
    return ll


def faire_lll (q) : 
    """lll prend une liste q et crée une liste de toutes les ll de q"""
    ll = faire_ll(q)        
    lll = []
    i = 0
    while(i*57*64<len(q)) :
        lll.append(faire_ll(isol(q,i,57*64)))  #insert toutes les ll dans lll
        i = i+1                           
    return lll


q = 'hsqjqdlqhabillagearmandeledouxpinatelbaptistejosuelefestoivaldavignondfgerragregooirentmgeraioislznbziuidnnksnshbdnnzkzakjhvlklsqgqkpîdhfaygicvbaonxispkfgdhivcbnuidfgrhezijgshjjdg,qhnkklsuqklkdjcnxbdghncvbnildkjxhhvnxbkjqsn,ghnsozlsdkhn'
print(faire_lll(q))



