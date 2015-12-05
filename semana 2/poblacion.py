import random, string
from individuo import Individuo

class Poblacion :

    def __init__ (self, individuos, genes) :
        self.max_individuos = individuos
        self.individuos     = [Individuo(genes) for _ in range(individuos)]


    def cruce (self, coeficiente = 0.5) :
        limite = len(self.individuos)
        conteo = int(limite * coeficiente)
        
        for i in range(conteo) :
            posicion    = random.randint(0, limite - 1)
            individuo_1 = self.individuos[posicion]
            posicion    = random.randint(0, limite - 1)
            individuo_2 = self.individuos[posicion]

            hijo = individuo_1.cruzar(individuo_2)

            self.individuos.append(hijo)

    def mutacion (self, coeficiente = 0.5) :
        limite = len(self.individuos)
        conteo = int(limite * coeficiente)
        
        for i in range(conteo) :
            posicion = random.randint(0, limite - 1)
            self.individuos[posicion].mutar()


    def torneo (self, fitness, coeficiente = 0.5) :
        limite = self.max_individuos
        lista  = []
        i      = 0

        self.ordenar_por_fitness(fitness)

        while len(lista) < limite :

            elegir = random.random()

            if elegir < coeficiente :
                lista.append(self.individuos[i])
                              
            i = (0, i+1)[i < limite - 1]

        self.individuos = lista


    def ordenar_por_fitness(self, fitness) :

        self.individuos = sorted(self.individuos, key=lambda individuo: individuo.fitness(fitness))


    def campeon (self, fitness) :
        campeon = self.individuos[0]

        if campeon.obtPares() == fitness :
            return True
        else :
            return False


    def generacion (self, fitness, coeficiente_cruce = 0.5, coeficiente_mutacion = 0.5, coeficiente_torneo = 0.5) :

        self.torneo(fitness, coeficiente_torneo)
        self.cruce(torneo_cruce)
        self.mutacion(coeficiente_mutacion)
        self.ordenar_por_fitness(fitness)
