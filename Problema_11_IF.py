# Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau
# IMPAR. Exemplu : Date de intrare : 45 3 24 Date de ieşire : 45 impar 3 impar 24 par
# primul nr=x; al doilea nr=y; al treilea nr=z;
x=int(input('Introdu primul nr:'))
y=int(input('Introdu al doilea nr:'))
z=int(input('Introdu al treilea nr:'))
if x%2==0:
    print(x, 'par')
else:
    print(x, 'impar')
if y%2==0:
    print(y, 'par')
else:
    print(y, 'impar')
if z%2==0:
    print(z, 'par')
else:
    print(z, 'impar')