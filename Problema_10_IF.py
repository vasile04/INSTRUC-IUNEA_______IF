# La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
# fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
# afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
# numărul de boabe de porumb. Exemplu: Date de intrare 100 4050 Date de ieşire: Curcanul mai mult cu 10 boabe.
# nr de gaini= ng; nr de boabe= nb
ng=int(input('Introdu nr de gaini de la ferma: '))
nb=int(input('Introdu nr de boabe de porumb: '))
if nb%ng==0:
    print('Curcanul și găinile mănâncă același nr de boabe')
if nb%ng!=0:
    print('Curcanul mănâncă cu', nb%ng, 'boabe mai mult')
