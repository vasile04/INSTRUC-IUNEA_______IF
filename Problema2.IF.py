# a=latura1; b=latura2; c=latura3
a=int(input('introdu lungimea primei lature:'))
b=int(input('Introdu lungimea laturei a doua:'))
c=int(input('Introdu lungimea laturei a treia:')) 
if (a<32000) and (b<32000) and (c<32000):
    if (a<b+c) and(b<a+c) and (c<b+a):
        print('da')
    else:
        print ('nu')