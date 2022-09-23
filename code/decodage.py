def concat (l1, l2) :
    for i in l2 :
        l1.append(i)
def assemble (lll) :
    """takes in argument the list of all the lists that contains 64 lists of 57 elements"""
    sequence = []
    for ll in lll :
        print(ll)
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