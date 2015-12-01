import random, string

class Individuo :

    def __init__ (self, length, choice = 'AB') :
        self._genoma = ''.join([random.choice(choice) for _ in range(length)])

    def obtPares (self) :
        pair = 0

        if len(self._genoma) < 2 :
            return pair

        for (i, gen) in enumerate(self._genoma) :
            if gen == 'B' :
                continue

            sub_genoma = self._genoma[(i + 1):]
            sub_genoma = sub_genoma.replace('A', '')

            pair += len(sub_genoma)

        return pair

    def hijo (self, pareja) :
        genoma_hijo = ''
        genoma_1    = self._genoma
        genoma_2    = pareja._genoma

        for (i, gen) in enumerate(self._genoma) :
            if genoma_1[i] == genoma_2[i] :
                genoma_hijo += genoma_1[i]
            else :
                choice       = ''+ genoma_1[i] + genoma_2[i] +''
                genoma_hijo += random.choice(choice)

        hijo         = Individuo(len(self._genoma))
        hijo._genoma = genoma_hijo

        return hijo

    def mutar (self) :
        array    = list(self._genoma)
        posicion = random.randint(0, len(self._genoma)-1)

        if array[posicion] == 'A' :
            array[posicion] = 'B'
        else :
            array[posicion] = 'A'

        self._genoma = "".join(array)

    def fitness (self, k) :
        pair = self.obtPares()

        fitness = k - pair

        if fitness < 0 :
            fitness *= -1

        return fitness
