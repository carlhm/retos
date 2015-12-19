
import random
import string
import math

class Individuo :
    
    def __init__(self, genes, choice = 'AB') :
        # crea gen nuevo o asigna uno dado
        if isinstance(genes, int) :
            self.genoma = [random.choice(choice) for _ in range(genes)]
        else :
            self.genoma = genes

        self.choice = choice
        self.longitud = len(self.genoma)

    def cruzar(self, pareja) :
        genoma_1 = self.genoma
        genoma_2 = pareja.genoma
        genoma_hijo = []
        # forma genoma en base a parecidos y discrepancias, gen a gen
        for (i, gen) in enumerate(self.genoma) :
            if genoma_1[i] == genoma_2[i] :
                genoma_hijo.append(genoma_1[i])
            else :
                # Azar entre gen de cada individuo
                choice = genoma_1[i] + genoma_2[i]
                genoma_hijo.append(random.choice(choice))

        hijo = Individuo(genoma_hijo)

        return hijo

    def mutar(self) :
        # variamos solo un caracter del genoma
        genoma = self.genoma
        posicion = random.randrange(self.longitud)
        # eliminamos anterior gen de los posibles
        choice = self.choice.replace(genoma[posicion], '')
        genoma[posicion] = random.choice(choice)

    def fitness(self, k) :
        pares = self.obt_pares()
        # distancia entre dos puntos (pares, k)
        fitness = math.sqrt((k - pares)**2)

        return fitness

    def obt_pares(self) :
        pares = 0
        genoma = self.genoma

        if self.longitud < 2 :
            return pares
        for (i, gen) in enumerate(genoma) :
            # por cada A
            if gen == 'B' :
                continue
            # cuenta numero de B a continuacion
            sub_genoma = genoma[(i + 1):]
            pares += sub_genoma.count('B')

        return pares

    def obt_genoma_ruido(self) :
        ruido = 0
        gen_cambio = self.genoma[0]

        for gen in self.genoma :
            if gen == gen_cambio :
                continue
            gen_cambio = gen
            ruido += 1
        
        return float(ruido)/float(self.longitud)

    def copia(self) :
        return Individuo(list(self.genoma))

    def traza(self) :
        return "P:%i R:%.3f > %s" % (self.obt_pares(), 
                                     self.obt_genoma_ruido(), 
                                     self)

    def __str__(self) :
        return "".join(self.genoma)

    @staticmethod
    def max_k(n) :
        # A0,...,A(n/2),B(1+n/2),...,Bn
        izqda_genoma = 'A'*(int(n/2))
        if (n % 2) == 1 :
            n += 1
        drcha_genoma = 'B'*(int(n/2))
        genoma = list('%s%s' % (izqda_genoma, drcha_genoma))
        individuo = Individuo(genoma)

        return individuo.obt_pares()
