import string, sys
from datetime     import datetime
from r2_poblacion import Poblacion

n = int(sys.argv[1])
k = int(sys.argv[2])

if k >= 0 and k <= ((n*(n-1))/2) and n >= 2 and n <= 50 :

    p        = Poblacion(n, k, int(n/2)*10)
    i        = 1
    h_inicio = datetime.now()

    print 'Individuos: '+ str(len(p._individuos))
    print 'G.'+ str(0) +" > "+ p._individuos[0]._genoma +" ("+ str(p._individuos[0].obtPares()) +")"

    while not p.campeon(k) :

        p.generacion(k)

        i += 1

        print 'G.'+ str(i-1) +" > "+ p._individuos[0]._genoma +" ("+ str(p._individuos[0].obtPares()) +")"

    h_fin = datetime.now()

    print 'Tiempo: '+ str((h_fin - h_inicio).total_seconds()) +' seg'