# Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
# câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
# numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
# Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
# bilelor: 17 Mari: 11 bile Verzi: 7 bile 
# m=bilele mici; b=bilele mari
#nr bile albe mici= ma; nr de bile rosii mici=mr; nr de bile verzi mici=mv; nr de bile mici de tot=mtot, mr total de bile rosii=R, Nr total de bile albe=A
# nr de bile albe mari=ba; nr de bile rosii mari=br; nr de bile verzi mari=bv; TOTALUL DE BILE =t, nr de bile mari total=btot, nr total de bile verzi=V
ma=int(input('Introdu nr de bile albe mici: '))
mr=int(input('Introdu nr de bile rosii mici: '))
mv=int(input('Introdu nr de bile verzi mici: '))
ba=int(input('Introdu nr de bile albe mari: '))
br=int(input('Introdu nr de bile rosii mari: '))
bv=int(input('Introdu nr de bile verzi mari: '))
mtot=ma+mr+mv
btot=ba+br+bv
A=ma+ba
R=mr+br
V=mv+bv
if mtot>btot:
    print('Nr de bile mici:', mtot, 'este mai mare decât cel al bilelor mari: ', btot)
else:
    print('Nr de bile mari:', btot, 'este mai mare decât cel al bilelor mici:', mtot)
if (A>R) and (A>V):
    print('Nr de bile mai numeroase este a celor albe cu:', A, 'bile')
if (R>A) and (R>V):
    print('Nr de bile mai numeroase este a celor rosii cu:', R, 'bile')
if (V>A) and (V>R):
    print('Nr de bile mai numeroase este a celor verzi cu:', V, 'bile')   
t=ma+mr+mv+ba+br+bv
print('nr total de bile de pe masa este de:', t, 'bile')    


