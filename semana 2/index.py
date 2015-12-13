import string
import random
import sys

from datetime import datetime
from individuo import Individuo
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

k_maxima = Individuo.max_k(n)

# limites iniciales
if k < 0 or k > ((n*(n-1))/2) or k > k_maxima or n < 2 or n > 50 :
    exit()

individuos = int(n**1.6)
poblacion = Poblacion(individuos, n)
generacion = Generacion(poblacion)
h_inicio = datetime.now()

print 'Individuos: %i' % (individuos)
# evoluciona la poblacion hasta alcanzar el fitness
while not poblacion.campeon(k) :
    generacion.ronda(k, 0.30, 0.5, 0.75)
# mostrar mejor individuo
print generacion.traza()
# mostrar el tiempo de ejecicion
h_fin = datetime.now()
print "Tiempo: %f seg" % ((h_fin - h_inicio).total_seconds())
