# Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
# ce clasa va fi repartizat (A, B, C, D sau E)?. Exemplu : date de intrare : x=73 date de ieşire : C.
# DEOARECE SE FORMEAZA 5 CLASE A cate 25 elevi=> nr total de elevi ntot=5*25 
ntot=5*25
print('Nr total de elevi din clasele a cincea este de:', ntot, 'elevi')
x=int(input('introdu pe al catulea loc este Radu:'))
if (x>=1) and (x<=25):
    print('Radu va fi in clasa a V-a "A"')
if (x>=26) and (x<=50):
    print('Radu va fi in clasa a V-a "B"')
if (x>=51) and (x<=75):
    print('Radu va fi in clasa a V-a "C"')
if (x>=76) and (x<=100):
    print('Radu va fi in clasa a V-a "D"')
if(x>=101) and (x<=ntot):
    print('Radu va fi in clasa a V-a "E"')
if (x>ntot):
    print('Eroare')
