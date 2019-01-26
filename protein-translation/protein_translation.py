
b = {'AUG' : 'Methionine' , 'UUU' : 'Phenylalanine' , 
'UUC' : 'Phenylalanine' , 'UUA' : 'Leucine' , 'UUG' : 'Leucine'
, 'UCU' : 'Serine' , 'UCC' : 'Serine' , 'UCA' : 'Serine' ,
'UCG' : 'Serine' , 'UAU' : 'Tyrosine' , 'UAC' : 'Tyrosine'
, 'UGU' : 'Cysteine' , 'UGC' : 'Cysteine' , 'UGG' : 'Tryptophan'
, 'UAA' : 'Stop' , 'UAG' : 'Stop' , 'UGA' : 'Stop'}


def proteins(strand):
    import re
    import itertools
    from collections import OrderedDict
    s=[]
    if type(strand) == str :
        strand = [strand[i:i+3] for i in range(0, len(strand), 3)]
        for i in strand:
            s += [value  for (key , value) in b.items() if re.match(key , i) != None]
            z = itertools.takewhile(lambda value : value != 'Stop' , s)
        return list(OrderedDict.fromkeys(z))    
    else : 
        s += [value  for (key , value) in b.items() if re.match(key , (''.join(strand))) != None ]
        z = itertools.takewhile(lambda value : value != 'Stop' , s)
        return list(OrderedDict.fromkeys(z))
        

