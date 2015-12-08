import string
import random
import sys

from datetime import datetime
from individuo import Individuo
from poblacion import Poblacion
from generacion import Generacion

def limite_max_k(n, k) :
    i_genoma = 'A'*(int(n/2))
    if (n % 2) == 1 :
        n += 1
    f_genoma = 'B'*(int(n/2))
    genoma = list('%s%s' % (i_genoma, f_genoma))
    individuo = Individuo(genoma)

    return individuo.obt_pares()

# Entrada definida
try :
    n = int(sys.argv[1])
except :
    exit()
try :
    k = int(sys.argv[2])
except :
    exit()

k_maxima = limite_max_k(n, k)

# Condiciones iniciales
if k >= 0 and k <= ((n*(n-1))/2) and k <= k_maxima and n >= 2 and n <= 50 :

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
