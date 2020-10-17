# Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
# exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. Exemplu : Date
# de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani. 
# ZIUA CURENTA=zc; luna curenta=lc; anul curent=ac; data curanta=dc
# ziua nasterii=zn; luna nașterii=ln ; anul nașterii=an; data nasterii=dn
ac=int(input('Introdu anul curent: '))
lc=int(input('introdu luna curenta: '))
zc=int(input('introdu ziua curenta: '))
an=int(input('Introdu anul nasterii: '))
ln=int(input('Introdu luna nasterii: '))
zn=int(input('Introdu ziua nasterii: '))
if lc==ln:
    if (zc>zn) or (zn==zc):
        print(ac-an,  'ani')
    else:
        print(ac-an-1, 'ani')
elif lc>ln:
    print(ac-an, 'ani')
else:
    print(ac-an-1, 'ani')     
