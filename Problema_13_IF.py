# La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
# secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
# rosie.
# deoarece sunt 4 culori => o culoare se va oferi la 25 
x=int(input('Introdu locul pe care l-a ocupat Ionel:'))
if (x>=1) and (x<=100):
    if (x>=1) and (x<=25):
        print('Ionel a castigat un tricou alb')
    if (x>=26) and (x<=50):
        print('Ionel a castigat un tricou roșu' )
    if (x>=51) and (x<=75):
        print('Ionel a castigat un tricou albastru')
    if (x>=75) and (x<=100):
        print('Ionel a castigat un tricou negru')