#Primul nr=n1; al doilea nr=n2; al treilea nr=n3; nr cel mai mare=m
n1=int(input('Introdu primul nr:'))
n2=int(input('Introdu al doilea nr:'))
n3=int(input('Introdu al treilea nr:'))
if (n1>0) and (n2>0) and (n3>0):
    m= max(n2, n3)
    print(m)
else:
    s=n1+n2
    print('Suma primelor două numere este:', s )