import random
import string

from individuo import Individuo

class Poblacion :

    def __init__(self, individuos, genes) :
        self.max_individuos = individuos
        self.individuos = [Individuo(genes) for _ in range(individuos)]


    def cruce(self, coeficiente=0.5) :
        limite = len(self.individuos)
        conteo = int(limite * coeficiente)
        
        for i in range(conteo) :
            # elegimos al azar que parejas cruzar
            posicion = random.randint(0, limite - 1)
            individuo_1 = self.individuos[posicion]
            posicion = random.randint(0, limite - 1)
            individuo_2 = self.individuos[posicion]
            # obtenemos descendiente, incrementeando inviduos
            hijo = individuo_1.cruzar(individuo_2)
            self.individuos.append(hijo)

    def mutacion(self, coeficiente=0.5) :
        limite = len(self.individuos)
        conteo = int(limite * coeficiente)
        # mutamos n individuos aleatorios segun el coeficiente
        for i in range(conteo) :
            posicion = random.randint(0, limite - 1)
            self.individuos[posicion].mutar()

    def torneo(self, fitness, coeficiente=0.5) :
        limite = self.max_individuos
        lista = []
        i = 0
        # ordenamos individuos de mejor a peor fitness
        self.ordenar_por_fitness(fitness)
        # siempre el mismo numero de individuos
        while len(lista) < limite :
            # sobrevive individuo si esta en el %
            elegir = random.random()
            if elegir < coeficiente :
                # agregamos duplicado a la nueva lista
                genoma = self.individuos[i].genoma
                clon = Individuo(list(genoma))
                lista.append(clon)
            # si son pocos vuelta a empezar la lista                  
            i = (0, i+1)[i < limite - 1]

        self.individuos = lista

    def ordenar_por_fitness(self, fitness) :
        # ordenar individuos en base a su fitness
        self.individuos = sorted(self.individuos, 
                                 key=lambda individuo: individuo.fitness(fitness)
                                 )

    def campeon(self, fitness) :
        return self.individuos[0].obt_pares() == fitness

    def obt_campeon(self) :
        return self.individuos[0]
