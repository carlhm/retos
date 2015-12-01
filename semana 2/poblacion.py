import random, string
from individuo import Individuo

class Poblacion :

    def __init__ (self, n, individuos = 10, cruce = 0.5, mutacion = 0.5, torneo = 0.75) :
        self._individuos = [Individuo(n) for _ in range(individuos)]
        self._mutacion   = mutacion
        self._cruce      = cruce
        self._torneo     = torneo

    def cruce (self) :
        conteo = int(len(self._individuos) * self._cruce)
        
        for i in range(conteo) :
            posicion    = random.randint(0, len(self._individuos)-1)
            individuo_1 = self._individuos[posicion]
            posicion    = random.randint(0, len(self._individuos)-1)
            individuo_2 = self._individuos[posicion]

            hijo = individuo_1.hijo(individuo_2)

            self._individuos.append(hijo)

    def mutacion (self) :
        conteo = int(len(self._individuos) * self._mutacion)
        
        for i in range(conteo) :
            posicion = random.randint(0, len(self._individuos)-1)
            self._individuos[posicion].mutar()


    def torneo (self) :
        lista = []
        i     = 0

        while len(lista) < len(self._individuos) :
            elegir = random.random()

            if elegir < self._torneo :
                lista.append(self._individuos[i])
                              
            i = (0, i+1)[i < len(self._individuos)-1]


        self._individuos = lista

    def ordenar_por_fitness(self, k) :
        self._individuos = sorted(self._individuos, key=lambda individuo: individuo.fitness(k))

    def campeon (self, k) :
        campeon = self._individuos[0]

        if campeon.obtPares() == k :
            return True
        else :
            return False
