# Sa se creeze un program ce va afișa soluțiile unei ecuații de gradul 2
# descriminantul ecuatiei= delta=d; x1,x2=soluțiile ecuației
# daca 2*a=0 => eroare a limbajului de programare 
import math
a=float(input('Introdu valoarea lui a:'))
b=float(input('Introdu valoarea lui b: '))
c=float(input('Introdu valoarea lui c: '))
d=b**2-1*4*a*c
print('d=b**2-1*4*a*c=', d)
if d<0:
    print('Ecuatia nu are solutii')
if d==0:
    print('x1=x2=', (-1*b+math.sqrt(d))/(2*a) )
if d>0:
    print(math.sqrt(d))
    x1=(-1*b-math.sqrt(d))/(2*a)
    x2=(-1*b+math.sqrt(d))/(2*a)
    print('x1=', x1)
    print('x2=', x2)
if (2*a==0):
    print('x1=x2=0')

