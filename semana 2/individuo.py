import random
import string

class Individuo :

    def __init__(self, num_genes, genoma = '', choice = 'AB') :

        if num_genes > len(genoma) :
            self.genoma = [random.choice(choice) for _ in range(num_genes)]
        else :
            self.genoma = genoma

        self.choice = choice
        

    def obtPares(self) :
        pair   = 0
        genoma = ''.join(self.genoma)

        if len(genoma) < 2 :
            return pair

        for (i, gen) in enumerate(genoma) :
            if gen == 'B' :
                continue

            sub_genoma = genoma[(i + 1):]
            pair      += sub_genoma.count('B')

        return pair


    def cruzar(self, pareja) :
        genoma_1    = self.genoma
        genoma_2    = pareja.genoma
        genoma_hijo = list(genoma_1)

        for (i, gen) in enumerate(self.genoma) :
            if genoma_1[i] == genoma_2[i] :
                continue
                
            choice         = genoma_1[i] + genoma_2[i]
            genoma_hijo[i] = random.choice(choice)

        hijo = Individuo(len(self.genoma), genoma_hijo)

        return hijo


    def mutar(self) :
        genoma   = self.genoma
        posicion = random.randint(0, len(genoma)-1)

        choice           = self.choice.replace(genoma[posicion], '')
        genoma[posicion] = random.choice(choice)

        self.genoma = genoma


    def fitness(self, k) :
        pair = self.obtPares()

        fitness = k - pair

        if fitness < 0 :
            fitness *= -1

        return fitness
