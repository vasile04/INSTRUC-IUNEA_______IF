# Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
# Exemplu : date de intrare : n=69 date de ieşire : casuta 17.
x=int(input('Introdu al câtulea a venit Ionel:'))
if x<=4:
    print('Ionel va fi cazat in 1 căsuță ')
else:
    print('Ionel va fi cazat in casuta: ', (x//4)+1)