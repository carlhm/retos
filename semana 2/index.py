import string, sys
from poblacion import Poblacion

n = int(sys.argv[1])
k = int(sys.argv[2])

if k >= 0 and k <= ((n*(n-1))/2) and n >= 2 and n <= 50 :

    p = Poblacion(n, int(n/2)*10)
    i = 1

    p.ordenar_por_fitness(k)

    print int(n/3)*10
    print str(0) +" : "+ p._individuos[0]._genoma +" : "+ str(p._individuos[0].obtPares())

    while not p.campeon(k) :

        p.torneo()
        p.cruce()
        p.mutacion()
        p.ordenar_por_fitness(k)

        i += 1

    print str(i-1) +" : "+ p._individuos[0]._genoma +" : "+ str(p._individuos[0].obtPares())