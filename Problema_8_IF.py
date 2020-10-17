# Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. Exemple : Date de intrare 23 45 Date de
# ieşire nu exista numar par ; Date de intrare 28 14 Date de ieşire 28 ; Date de intrare 77 4 Date de ieşire 4.
# cel mai mare nr=m
n1=int(input('Introdu primul numar:'))
n2=int(input('Introdu al doilea numar:'))
if (n1%2==0) and (n2%2==0):
    m=max(n1, n2)
    print(m)
if (n1%2==0) and (n2%2!=0):
    print(n1)
if (n1%2!=0) and (n2%2!=0):
    print('Niciunul dintre numerele introduse este par')   

