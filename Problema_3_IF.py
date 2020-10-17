# Să se verifice dacă o literă introdusă este vocală sau consoană. Exemplu : Date de intrare a Date de ieşire vocala.
# litera=l
l=str(input('Introduceti o litera:'))
if ((l=="a") or (l=="e") or (l=="i") or (l=="o") or (l=="u") or (l=="y") or(l=="ă") or (l=="î") or (l=="â")):
    print('litera', l,  'este o vocala')
else:
    print('Litera', l,  'este consoana') 
