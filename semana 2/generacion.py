from poblacion import Poblacion

class Generacion :

    def __init__(self, poblacion) :

        self.poblacion = poblacion
        self.num_ronda = 0


    def ronda(self, fitness, 
                coeficiente_cruce    = 0.5, 
                coeficiente_mutacion = 0.5, 
                coeficiente_torneo   = 0.5) :

        self.poblacion.torneo(fitness, coeficiente_torneo)
        self.poblacion.cruce(coeficiente_cruce)
        self.poblacion.mutacion(coeficiente_mutacion)

        self.num_ronda += 1


    def traza(self) :
        
        campeon = self.poblacion.obt_campeon()

        traza   = 'G.'  + str(self.num_ronda)
        traza  += ' > ' + "".join(campeon.genoma)
        traza  += ' ('  + str(campeon.obtPares())   + ")"

        print traza
