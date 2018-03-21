def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    #print (seqs)
    res = []
   # print (seqs)
    while all(seqs):
        print (' in while')
        for s in seqs:
            print ('in for')
            print('s is :' , s)
            t = s.pop(0),
            
        res.append(t)
    return res

"""
def mymapPad(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        for s in seqs:
            """
