lugar = 'inicio'
amor = 0
regalos = 0
game_runnig = True
while game_runnig:
    if lugar == 'inicio':
        print("Bienvenido a Kiss Love, un juego de citas, donde tu objetivo principal sera conquistar a la heroina principal, suerte con eso")
        print("Para empezar el juego pon '1', si quieres cerrar el juego pon '2'")

        respuesta = input("1-2: ")

        if respuesta == "1":
            print("Bienvenido, espero que lo disfrutes")
            lugar = "casa"
        elif respuesta == "2":
            print("Esta bien, Adiooss")
            game_runnig = False
        else:
            print("Invalido")

    elif lugar == "casa":
        print("Son las 6 a.m, tu reloj depertador empieza a sonar como loco")
        print("El ruido es tan fuerte que no puedes evitar despertarte")
        print("Tu: Ughhhh, Muy bien, a iniciar otro dia mas")
        print("Procedes a levantarte y mirarte al espejo, y ahi estas tu Marcell Fuertes, un estudiante comun y corriente de 17 años, que asiste a la preparatoria SLG")
        print("Miras con detalle tu cara, te fijas en tus grandes ojeras, las cuales seguramente las ganaste por jugar videojuegos toda la noche, tambien miras tu herida de guerra, y recuerdas lo que paso en ese triste dia")
        print("Tu: Algun día volveremos a vernos ########### y esta vez te dire mis sentimientos como se debe...")
        print("Vez la hora, y te sorprendes al saber lo tarde que es")
        print("Tu: Rayos debo ir rapido a la preparatoria o esta vez no me dejaran entrar, pero aun no he desayunado y me ha entrado demasiada hambre, ¿que debeira hacer?")
        print("Decide, pon '1' para rapidamente comer tu desayuno, pon '2' para no comer tu desayuno y ir a la preparatoria")

        respuesta = input("1-2: ")

        if respuesta == "1":
            print("Decides comer tu desayuno y corre a la preparatoria")
            lugar = "preparatoria"
        elif respuesta == "2":
            print("Decides dejar tu desayuno a un lado y correr a la preparatoria")
            lugar = "muerte1"
        else:
            print("Invalido")

    elif lugar == "muerte1":
        print("Ibas corriendo apresurado por la calle, directo a tu preparatoria, estabas un poco mareado, pues el sol estaba mas radiante que nunca y tu no comiste tu desayuno")
        print("De pronto te sientes muy cansado, y tus ojos se cierran poco a poco")
        print("Camion: PIIIIIIIIIIII")
        print("Antes de dormirte por completo, mientras caes, ves como un gran camion se va acercando a ti")
        print("Eso fue lo ultimo que Marcell Fuertes vio antes de morir")
        print("No puedes morir aun, tienes que encontrate con ########, por favor VIVE")
        print("Si quieres volver a empezar pon '1', si quieres terminar el juego pon '2' ")

        respuesta = input("1-2: ")

        if respuesta == "1":
            lugar = "casa"
        elif respuesta == "2":
            print("Si tan solo hubiera comido mi desayuno...")
            game_runnig = False
        else:
            print("Invalido")

    elif lugar == "preparatoria":
        print("Decides comer tu desayuno y ir a la preparatoria")
        print("Corres lo mas rapido que puedes, pero ves que las puertas estan cerradas y a tu profesor Joshua Villanecio parado en la entrada, con una mirada llena de ira")
        print("Joshua: Buenos dias señor Marcell, ahora con que excusa me va a venir esta vez")
        print("Tu: Perdon profe, se me acabron las excusas, jeje")
        print("Joshua: SABES LO VERGONZOSO QUE ES TENER QUE ESPERARTE AQUI TODAS LAS MAÑANAS, ACASO PIENSAS QUE NO TENGO NADA QUE HACER!!")
        print("Tu profesor te regaña, ya era la quinta vez en la semana, tu solo miras para abajo avergonzado")
        print("Tu: Esta bien profesor, esta vez se lo prometo, desde ahora llegare mas temprano!!")
        print("Le dices eso a tu profesor con una fulminante mirada en tus ojos")
        print("Joshua: Espero que no sea otra de tus promesas vacias, esta bien pasa")

        print("Entras a la preparatoria SLG, y te dirijes a tu aula")
        print("Todos tus compañeros te quedan mirando mientras caminas por los pasillos")
        print("Algunos murmuran cosas mientras te miran")
        print("Tu sabes muy bien el porque, hace 1 mes que volviste a venir a la preparatoria, luego de estar ausante durante mucho tiempo, te encerraste en tu habitacion despues de lo que ocurrio en ese fatidico día")
        print("Todos los rumores que se hicieron de ti a partir de ese dia, todas las personas que te traicionaron, ahora te consume poco a poco en el presente, aunque todos te odien, solo te queda el seguir adelante...")
        print("Ahora frente a ti tienes la gran puerta de tu aula, el aula '3 X' ")
        print("Entras al aula y te dirijes a tu asiento")
        print("Entonces sientes una presencia fuerte que se acerca a tus espaldas a un paso lento")
        print("Te preguntas quien es y decides regresar a ver")
        print("Duquesino: Hola amigo, que tal estas hoy?")
        print("Es tu amigo Duquesino Estebansino, tu unico amigo en la prepa")
        print("Ahora tu decides, como le responderas a tu amigo?")
        print("a. Hola, muy bien y tu?")
        print("b. Bah lo mismo de siempre, y tu que tal?")
        print("c. Largate, te odio")

        respuesta = input("a-c: ")

        if respuesta == "a":
            print("Estebansino: Muy bro, me alegro que estes bien, hoy demos lo maximo otra vez")
            print("Tu: Muy bien vamos bro")
            lugar = "salon"
        elif respuesta == "b":
            print("Estebansino: JAJAJAJA, no has cambiado nada eh?, hoy demos lo maximo tambien!")
            print("Tu: Vamos a darle")
            lugar = "salon"
        elif respuesta == "c":
            print("Estebansino: Uhhhh, esta bien amigo, perdoname por molestarte")
            print("Tu: ...")
            lugar = "callejon1"
        else:
            print("Invalido")

    elif lugar == "callejon1":
        print("Al terminar el colegio decides salir corriendo de la preparatoria, mientras caminabas a tu casa, te encuentras con los matones de tu curso")
        print("Sin duda el peor escenario posible, ahi estaba su lider parado")
        print("Sartin Mecolalde")
        print("Mecolalde: Ohh, miren a quien tenemos aqui, acaso no eres ese rarito que se la pasa solo todo el tiempo?")
        print("Random: De seguro que tiene un buen de dinero, vamos por que no compartes un poco")
        print("Decide, pon'a' para dar tu dinero, o pon 'b' para no dar tu dinero")

        respuesta = input("a-b: ")

        if respuesta == "a":
            print("Decides dar todo tu dinero, para tu mala suerte hoy no traias mucho")
            print("Mecolalde: Que es esta miseria, acaso te burlas de nosotros?!")
            print("Tu: N-no, de verdad es lo unico que tengo")
            print("Mecolalde: Mira basura, si no nos traes mas dinero para mañana haremos de tu vida un infierno, por el momento de vamos a dejar una advertencia")
            print("Chicos, denle una leccion")
            print("Te empiezan a golpear brutalmente, tratas de pedir ayuda, pero nadie viene a tu rescate")
            print("Mecolalde: en serio crees que alguien te va ayudar, tan solo me haces cabrear mas")
            print("De pronto ves como Mecolalde saca una navaja de su bolsillo y la acerca a ti")
            print("Mecolade: Nadie se burla de mi idiota")
            print("En una accion solo llevada por la ira, te apuñala, sientes un dolor terrible en tu estomage y empiezas a retorcerte")
            print("Mecolalde: Mierda, la cague, n-no era mi intencion")
            print("Sientes una segunda apuñalada en tu cuerpo, y asi varias veces")
            print("Estas casi muerto, lo unico que puedes escuchar son algo parecidos a voces, pero no las distingues bien")
            print("Lo hecho ya... Solo...vamo... corre")
            print("Poco tiempo despues Marcell Fuertes murio")
            print("No puedes rendirte aun, debes volver a encontrarte con #########, porfavor VIVE")
            print("Selecciona 'a' si quieres empezar de nuevo, presiona 'b' si quieres acabar el juego")

            respuesta = input ("a-b: ")

            if respuesta == "a":
                lugar = "preparatoria"
            elif respuesta == "b":
                print("Si tan solo hubiera sido mas amable")
                game_runnig = False
            else:
                print("Invalido")

        elif respuesta == "b":
            print("Decides no dar tu dinero y enfrentarte a ellos")
            print("Mecolalde: Que es lo que intentas imbecil, en serio crees que tienes lo necesario para ganarnos?")
            print("Corres desesperado, preparandote para darle un golpe en la cara a Mecolalde")
            print("Mecolalde: JAJAJAJ, idiota, acercate si es que puedes")
            print("Ves como Mecolalde saca una navaja de su bolsillo, en un impulso de ira, el te apuñala")
            print("Caes al suelo y te retuerces del dolor")
            print("Mecolalde: M-mierda no era mi in-intencion, e-estas bien?")
            print("Poco despues sientes otras varias puñaladas mas, el dolor es insoportable y poco a poco sientes que la llama de tu vida se apaga")
            print("Tan solo escuchas algo parecido a voces pero no las distingues bien")
            print("Huyamos...n...corre")
            print("Poco despues Marcell Fuertes murio")
            print("No puedes morir ahora, aun debes encontrarte con ########, por favor VIVE")
            print("Decide, pon 'a' si quieres volver a empezar, presiona 'b' si quieres terminar el juego")

            respuesta = input("a-b: ")

            if respuesta == "a":
                lugar = "preparatoria"
            elif respuesta == "b":
                print("Si tan solo hubiera sido mas amable")
                game_runnig = False
            else:
                print("Invalido")
    elif lugar == "salon":
        print("Te dirijes a tu asiento, tu amigo Estebansino esta sentado al frente tuyo")
        print("Estebansino: Escuchaste sobre que va a venir una estudiante transefirda hoy?")
        print("Tu: Uh?, en serio?")
        print("Estebansino, Sii, dicen que es una hermosura, que viene del extranjero, estoy emociando de que llegue")
        print("De pronto la puerta de tu salon se abre y entra una hermosa chica, tiene un pelo rubio brillante, sus ojos son de un profundo verde, sus pestañas son grandes y alargadas, y usa un maquillaje simple, aun asi era hermosa, en tu mente parece un angel caido del cielo")
        print("De pronto su profesora se para y se dirije a la chica y a todo el salon")
        print("Profesora: Como algunos sabran esta sera su compañera durante este año, por favor tratenla con respeto")
        print("Profesora: Por favor presentate")
        print("La chica nueva con su esbelta figura, agarra un marcador y escribe su nombre en el pizarron")
        print("???: Hola a todos me llamo Amira Ramirez, espero poder llevarme bien con todos este año")
        print("Profesora: Por favor sientate alli, donde esta el asiento libre")
        print("No puede ser, Amira se sentara a lado tuyo, tu mente empezo a dar vueltas y no sabias como reaccionar, deberia saludarla pensaste?")
        

