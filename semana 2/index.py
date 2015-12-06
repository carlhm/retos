import string, sys
from datetime   import datetime
from poblacion  import Poblacion
from generacion import Generacion

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
    p          = Poblacion(individuos, n)
    g          = Generacion(p)
    h_inicio   = datetime.now()

    print 'Individuos: '+ str(individuos)

    while not p.campeon(k) :

        g.ronda(k, 0.30, 0.5, 0.75)


    g.traza()

    h_fin = datetime.now()

    print 'Tiempo: '+ str((h_fin - h_inicio).total_seconds()) +' seg'