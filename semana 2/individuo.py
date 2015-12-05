import random, string

class Individuo :

    def __init__ (self, genes, genoma = '', choice = 'AB') :

        if genes > len(genoma) :
            self.genoma = ''.join([random.choice(choice) for _ in range(genes)])
        else :
            self.genoma = genoma

        self.choice = choice
        

    def obtPares (self) :
        pair = 0

        if len(self.genoma) < 2 :
            return pair

        for (i, gen) in enumerate(self.genoma) :
            if gen == 'B' :
                continue

            sub_genoma = self.genoma[(i + 1):]
            sub_genoma = sub_genoma.replace('A', '')

            pair += len(sub_genoma)

        return pair


    def cruzar (self, pareja) :
        genoma_hijo = ''
        genoma_1    = self.genoma
        genoma_2    = pareja.genoma

        for (i, gen) in enumerate(self.genoma) :
            if genoma_1[i] == genoma_2[i] :
                genoma_hijo += genoma_1[i]
            else :
                choice       = ''+ genoma_1[i] + genoma_2[i] +''
                genoma_hijo += random.choice(choice)

        hijo = Individuo(len(self.genoma), genoma_hijo)

        return hijo


    def mutar (self) :
        array    = list(self.genoma)
        posicion = random.randint(0, len(self.genoma)-1)

        if array[posicion] == 'A' :
            array[posicion] = 'B'
        else :
            array[posicion] = 'A'

        self.genoma = "".join(array)


    def fitness (self, k) :
        pair = self.obtPares()

        fitness = k - pair

        if fitness < 0 :
            fitness *= -1

        return fitness
