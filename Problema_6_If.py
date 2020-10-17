# Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate
# notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele
# luate şi afişaţi notele pe care le va comunica părinţilor. Exemple : Date de intrare 6 9 9 Date de ieşire 6 9 9 ; Date de
# intrare 8 5 7 Date de ieşire 8.
# PRIMA NOTA=n1; a doua nota=n2; a treia nota=n3; n4= nota cea mai mare 
n1=int(input('Introdu prima nota a lui Andrei: '))
n2=int(input('Iintrodu a doua nota a lui Andrei: '))
n3=int(input('Introdu a treia nota a lui Andrei: '))
1<n1<10
1<n2<10
1<n3<10
if (n3>=8):
    print('Notele pe care le va spune Andrei sunt:',n1, n2, n3)
else:
    n4 = max(n1, n2)
    print('Nota pe care o va spune parinților va fi:', n4)
