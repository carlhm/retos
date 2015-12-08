import string
import sys

from datetime import datetime
from poblacion import Poblacion
from generacion import Generacion

# Entrada definida
try :
    n = int(sys.argv[1])
except :
    exit()
try :
    k = int(sys.argv[2])
except :
    exit()

# Condiciones iniciales
if k >= 0 and k <= ((n*(n-1))/2) and n >= 2 and n <= 50 :

    individuos = int(n**1.65)
    p = Poblacion(individuos, n)
    g = Generacion(p)
    h_inicio = datetime.now()

    print 'Individuos: %i' % (individuos)
    # evoluciona la poblacion hasta alcanzar el fitness
    while not p.campeon(k) :
        g.ronda(k, 0.30, 0.5, 0.75)
    # mostrar mejor individuo
    g.traza()
    # mostrar el tiempo de ejecicion
    h_fin = datetime.now()
    print "Tiempo: %f seg" % ((h_fin - h_inicio).total_seconds())
