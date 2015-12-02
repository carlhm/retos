import random, string
from individuo import Individuo

class Poblacion :

    def __init__ (self, genes, fitness, individuos, cruce = 0.30, mutacion = 0.5, torneo = 0.75) :
        self._max_individuos = individuos
        self._individuos     = [Individuo(genes) for _ in range(individuos)]
        self._mutacion       = mutacion
        self._cruce          = cruce
        self._torneo         = torneo

        self.ordenar_por_fitness(fitness)

    def cruce (self) :
        limite = len(self._individuos)
        conteo = int(len(self._individuos) * self._cruce)
        
        for i in range(conteo) :
            posicion    = random.randint(0, limite - 1)
            individuo_1 = self._individuos[posicion]
            posicion    = random.randint(0, limite - 1)
            individuo_2 = self._individuos[posicion]

            hijo = individuo_1.cruzar(individuo_2)

            self._individuos.append(hijo)

    def mutacion (self) :
        limite = len(self._individuos)
        conteo = int(limite * self._mutacion)
        
        for i in range(conteo) :
            posicion = random.randint(0, limite - 1)
            self._individuos[posicion].mutar()


    def torneo (self) :
        limite = self._max_individuos
        lista  = []
        i      = 0

        while len(lista) < limite :

            elegir = random.random()

            if elegir < self._torneo :
                lista.append(self._individuos[i])
                              
            i = (0, i+1)[i < limite - 1]

        self._individuos = []
        self._individuos = lista

    def ordenar_por_fitness(self, fitness) :
        self._individuos = sorted(self._individuos, key=lambda individuo: individuo.fitness(fitness))

    def campeon (self, fitness) :
        campeon = self._individuos[0]

        if campeon.obtPares() == fitness :
            return True
        else :
            return False

    def generacion (seld, fitness) :

        seld.torneo()
        seld.cruce()
        seld.mutacion()
        seld.ordenar_por_fitness(fitness)
