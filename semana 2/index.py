import string, sys
from datetime  import datetime
from poblacion import Poblacion

def trazaGenerazion(poblacion, generacion_n) :

    print 'G.'+ str(generacion_n) +" > "+ poblacion._individuos[0]._genoma +" ("+ str(poblacion._individuos[0].obtPares()) +")"

# Entrada definida
try :
    sys.argv[1]
except IndexError :
    n = 0
else :
    n = int(sys.argv[1])
try :
    sys.argv[2]
except IndexError :
    k = -1
else :
    k = int(sys.argv[2])

# Condiciones iniciales
if k >= 0 and k <= ((n*(n-1))/2) and n >= 2 and n <= 50 :

    individuos = int(n**1.65)
    p          = Poblacion(individuos, n, k)
    i          = 1
    h_inicio   = datetime.now()

    print 'Individuos: '+ str(individuos)

    while not p.campeon(k) :

        p.generacion(k, 0.30, 0.5, 0.75)

        i += 1


    trazaGenerazion(p, i - 1)

    h_fin = datetime.now()

    print 'Tiempo: '+ str((h_fin - h_inicio).total_seconds()) +' seg'