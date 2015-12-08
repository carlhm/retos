import random
import string

class Individuo :

    def __init__(self, genes, choice = 'AB') :
        # crea gen nuevo o asigna uno dado
        if isinstance(genes, int) :
            self.genoma = [random.choice(choice) for _ in range(genes)]
        else :
            self.genoma = genes

        self.choice = choice

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
        genoma   = self.genoma
        posicion = random.randint(0, len(genoma)-1)
        # eliminamos anterior gen de los posibles
        choice = self.choice.replace(genoma[posicion], '')
        genoma[posicion] = random.choice(choice)

        self.genoma = genoma

    def fitness(self, k) :
        pair = self.obt_pares()

        fitness = k - pair
        # valores absolutos, n y -n estan igual de cerca de 0
        if fitness < 0 :
            fitness *= -1

        return fitness

    def obt_pares(self) :
        pair = 0
        genoma = self.to_string()

        if len(genoma) < 2 :
            return pair

        for (i, gen) in enumerate(genoma) :
            # por cada A
            if gen == 'B' :
                continue
            # cuenta numero de B a continuacion
            sub_genoma = genoma[(i + 1):]
            pair += sub_genoma.count('B')

        return pair

    def to_string(self) :
        return "".join(self.genoma)

