# Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. Exemplu : Date de
# intrare nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 Date de ieşire punctaj maxim are elevul cu nr crt 7
# PUNCTAJUL PRIMULUI ELEV=p1; numarul primului elev curent=e1
# punctajul elevului al doilea curent=p2; numarul celui de-al doilea elev curent=e2
# punctajul elevului al treilea curent=p3; numarul elevului al treilea curent=e3
e1=int(input('Introdu numărul primului elev curent: '))
e2=int(input('Introdu numarul celui de-al doilea elev curent:'))
e3=int(input('Introdu numarul celui de-al treilea elev curent:'))
p1=int(input('Introdu punctajul primului elev curent:'))
p2=int(input('Introdu punctajul celui de-al doilea elev curent:'))
p3=int(input('Introdu punctajul celui de-al treilea elev curent:'))
if (p1>p2) and (p1>p3) :
    print('Punctajul maximal are elevul', e1, 'cu', p1, 'puncte' )
if (p2>p3) and (p2>p1):
    print('Punctajul maximal are elevul', e2, 'cu', p2,  'puncte'  )
if (p3>p2) and (p3>p1) :
    print('Punctajul maximal are elevul', e3, 'cu', p3, 'puncte')   
