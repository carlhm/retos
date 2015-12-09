import string
import random
import sys

from datetime import datetime
from individuo import Individuo
from poblacion import Poblacion
from generacion import Generacion

def limite_max_k(n, k) :
    izqda_genoma = 'A'*(int(n/2))
    if (n % 2) == 1 :
        n += 1
    drcha_genoma = 'B'*(int(n/2))
    genoma = list('%s%s' % (izqda_genoma, drcha_genoma))
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
# limites iniciales
if k < 0 or k > ((n*(n-1))/2) or k > k_maxima or n < 2 or n > 50 :
    exit()

individuos = int(n**1.55)
p = Poblacion(individuos, n)
g = Generacion(p)
h_inicio = datetime.now()

print 'Individuos: %i' % (individuos)
# evoluciona la poblacion hasta alcanzar el fitness
while not p.campeon(k) :
    g.ronda(k, 0.30, 0.5, 0.75)
# mostrar mejor individuo
print g.traza()
# mostrar el tiempo de ejecicion
h_fin = datetime.now()
print "Tiempo: %f seg" % ((h_fin - h_inicio).total_seconds())
