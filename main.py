import random



class Big_Bang_Theory_game:
    # Metodo constructor
    def __init__(self):
        self.estado = "inicial"
        self.ronda = 0
        self.marcador = [0,0] # marcador [usuario,maquina]

    #*---------------------------------------------------------------------------------------------------------------------------
    # Variables de clase
    OPCIONES_MAQUINA = ["piedra","papel","tijeras","lagarto","spock"]
    OPCIONES_USUARIO = ["piedra","papel","tijeras","lagarto","spock","s"]
    GANA = {
        "piedra":{
            "lagarto":"La piedra aplasta al lagarto",
            "tijeras":"La piedra aplasta a la tijeras"
        },

        "papel":{
            "piedra":"El papel cubre la piedra",
            "spock":"El papel desautoriza a spock"
        },

        "tijeras":{
            "papel":"La tijeras corta el papel",
            "lagarto":"La tijeras decapita al lagarto"
        },

        "lagarto":{
            "spock":"El lagarto envena a spock",
            "papel":"El lagarto se come el papel"
        },

        "spock":{
            "piedra":"Spock vaporiza la piedra",
            "tijeras":"Spock rompe la tijeras"
        }
    }
    #*--------------------------------------------------------------------------------------------------------------------------
    

    #*-------------------------------------------------------------------------------------------------------------------------
    # Estado inicial del juego
    def inicial(self):

        if self.marcador[0] == 0 and self.marcador[1] == 0:
            print(f'''
            ****************************************************************************************************************************


                BIG BANG THEORY GAME
                Hola humano, mi nombre es Sheldom bot, soy un ser una inteligencia superior, quiero jugar contigo


            ''')

        # Input del usuario
        user_input = input("    >> piedra, papel, tijeras, lagarto, spock (s para salir o r para reiniciar marcador): ")

        # Si el usuario desea reiniciar juego, actualizamos las variables del objeto juego
        if user_input == "r":
            self.estado = "inicial"
            self.marcador = [0,0]
            self.ronda = 0
            print(f'''
                ******************************************************************************************************************
                    
                    
                    >>>>>>  Juego reiniciado
                    >>>>>>  Ronda 1
                    >>>>>>  Marcador [0, 0]


            ''')

        elif user_input in self.OPCIONES_USUARIO:
            self.estado = "jugando"
            return user_input

        else:
            print(f'''
            *********************************************************************************************************************


                ¡HEY HUMANO QUE HACES?! {user_input} NO ES UNA OPCION VALIDA
                Vuelve a intetarlo

                
            ***********************************************************************************************************************
            ''')
    #*-------------------------------------------------------------------------------------------------------------------------


    #*-------------------------------------------------------------------------------------------------------------------------
    # Metodo que valida si el usuario gana, pierde o empatan
    def jugando(self,user_input):

        # Hacemos que la maquina selecciona una opcion
        maquina = random.choice(self.OPCIONES_MAQUINA)
        game.estado = "inicial"

        if maquina in self.GANA[user_input]:
            # Si el usuario gana actualizamos el marcado a su favor
            self.marcador[0] += 1
            self.ronda += 1
            print(f'''
                *****************************************************************************************************************
                

                    Eres bueno humano, me has ganado: {self.GANA[user_input][maquina]}
                    MARCADOR DEL JUEGO: {self.marcador}
                    OPCION DE LA SHELDOM BOT: {maquina}
                    RONDA: {self.ronda}


            ''')
        elif maquina == user_input:
            self.ronda += 1
            print(f'''
                ****************************************************************************************************************


                Esta vez es un empate humano
                MARCADOR DEL JUEGO: {self.marcador}
                OPCION DE LA SHELDOM BOT: {maquina}
                RONDA: {self.ronda}


            ''')

        else:
            # Si gana la maquina actualizamos el marcador a favor de la maquina
            self.marcador[1] += 1
            self.ronda += 1
            print(f'''
                ******************************************************************************************************************
                

                ¡JAJAJAJAJAJAJ! Te he ganado humano {self.GANA[maquina][user_input]}
                MARCADOR DEL JUEGO: {self.marcador}
                OPCION DE LA SHELDOM BOT: {maquina}
                RONDA: {self.ronda}


            ''')    
    #*-------------------------------------------------------------------------------------------------------------------------
        



if __name__ == '__main__':
    #****************Intanciamos la clase****************
    game = Big_Bang_Theory_game()

    # Maquina de estados finitos
    while True:

        # Si la maquina se encuentra en estado inicial se ejecuta el metodo encargado de saludar al usuario y pedirle el la opcion
        if game.estado == "inicial":
            opcion_usuario = game.inicial()

            if opcion_usuario == "s":
                print(f'''
                    Ahhh yo queria jugar                
                ''')
                break

        # Si el valor ingresado por el usuario es valido, la maquina pasa al estado jugando
        if game.estado == "jugando":
            game.jugando(opcion_usuario)