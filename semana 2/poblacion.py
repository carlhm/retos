import random, string
from individuo import Individuo

class Poblacion :

    def __init__ (self, individuos, genes, fitness) :
        self._max_individuos = individuos
        self._individuos     = [Individuo(genes) for _ in range(individuos)]

        self.ordenar_por_fitness(fitness)

    def cruce (self, coeficiente = 0.5) :
        limite = len(self._individuos)
        conteo = int(len(self._individuos) * coeficiente)
        
        for i in range(conteo) :
            posicion    = random.randint(0, limite - 1)
            individuo_1 = self._individuos[posicion]
            posicion    = random.randint(0, limite - 1)
            individuo_2 = self._individuos[posicion]

            hijo = individuo_1.cruzar(individuo_2)

            self._individuos.append(hijo)

    def mutacion (self, coeficiente = 0.5) :
        limite = len(self._individuos)
        conteo = int(limite * coeficiente)
        
        for i in range(conteo) :
            posicion = random.randint(0, limite - 1)
            self._individuos[posicion].mutar()


    def torneo (self, coeficiente = 0.5) :
        limite = self._max_individuos
        lista  = []
        i      = 0

        while len(lista) < limite :

            elegir = random.random()

            if elegir < coeficiente :
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

    def generacion (seld, fitness, coeficiente_cruce = 0.5, coeficiente_mutacion = 0.5, coeficiente_torneo = 0.5) :

        seld.torneo(coeficiente_torneo)
        seld.cruce(torneo_cruce)
        seld.mutacion(coeficiente_mutacion)
        seld.ordenar_por_fitness(fitness)
