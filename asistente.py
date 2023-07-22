# abrimos el cmd de windows vamos utilizar  librerias
# pip install SpeechRecognition -> tomar todo lo que le decimos a la computadora y convertirlo a texto 
# pip install pyttsx3 ->  va aser que nuestra computadora empieze a hablar para que puede hablar tambien debemos instalar -> pip install pyAudio  
# pip install pywhatkit  -> tomar nuestro asistente virtual y darle "poder" lo que va aser es  darle funcione como si abre youtube tal cancion "es a su uso que lo vamos a necesitar"
# pip install wikipedia -> va a ayudar para conectarnos con wikipedia y aser que nuestro asistente sepa cosas , si lee decimos que busca algo lo va a buscar y no los va a decir 
# pip install pygame  -> nos sirve para crear videojuegos en ptython vamos a usar un modulo 
# pip install keyboard -> a usar nuestro teclado y python lo pueda usar dar un uso 
# speech_recognition tomar lo que decimos y convertirlo  a texto
import speech_recognition as sr  # primero importaremos la libreria speech_recognition y le daremos un alias que de nosotros es "sr"
# para darle funcion para que nuestra ordenador hable, pyttsx3
# darle funcion poder para que lo hagA AUTOMATIco automatizado buscar sin nosotros no darle click , pywhatkit
#  conectarnos con el wikipedia y aser que lo que decimos lo busce y darnos una respuesta es como darle una preguntab  pero por voz lo transforma  a texto y nos dara una informacion y nos la bolvera hablando y por consola,wikipedia
# en python viwne instalados varios modulos y en ello el date time que nos sirvira oara horas minutos  , fechas todo lo que viene de tiempo auto matizarlos , etc,datetime
#  nos permite lanzar un listener o escuchador que es un hilo de ejecucion que esta monitorizzando el teclado ,keyboard
import subprocess as sub  # iocinos
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, colors, os # y tamien importaremos las otras librerias pyttsx3, pywhatkit , wikipedia, datetime, keyboard 
from pygame import mixer # pigname = usaremos un modulm de  ello : mixer = 

name = "Omar"  # crearemos un nombre para nuestro asistente puede  ser opcional en este caso lo puse mi nombre
listener = sr.Recognizer()  # con el sr.Recognizer() le estamos diciendo que empiese a reconocer y le asignamos a la variable listener
engine = pyttsx3.init()  # otra variable lla,ada engine iniciamos nuestra libreria pyttsx3.init() 

voices = engine.getProperty('voices')  # creamos una variable voices llamamos a la variable engine y obtener la propiedad voices
engine.setProperty('voices', voices[0].id) # lo que estamos asiendo con la propiedad de setProperties es tomar la propiedad de voices de engine y ponerle la voz que esta en el indice 0 y junto con su id
engine.setProperty('rate', 145)

sites = {
                'google':'google.com',
                'youtube':'youtube.com',
                'facebook':'facebook.com',
                'mensaje':'web.whatsapp.com',
                'cursos':'freecodecamp.org/learn',
                'musica':'https://www.youtube.com/watch?v=GEaVO8tpmmw'
            }

files = {
    'carta':'escrito.txt',
    'entra':'comunicado.pdf',
    'foto':'64_OmarRivera_C2.png'
}
# crear 3 funciones para que nos van a ayudar a crear nuestro asistente virtual 
# primera funcion talk
def talk(text):  # la vamos a llamar talk  y siempre ponerle la identancion 
    engine.say(text)  # todo lo que pongamos en este parentesis con el metodo say la computadora va hablar el texto que agarra lo va a convertir en voz 
    engine.runAndWait()  # para ello funcione tambien es esta linea que es engine.runAndWait() Que lo que va aser es que corra y que espere y con esto estara construida nuestra funcion de talk 
# segunda funcion listen
def listen(): # listen de escuchar crearemos un tryCash para ccrear un tryCash lo que tenemos que hacer es poner la palabra try y except el tryCash es una forma de ver de que todo vaya bien todo lo que escribamos que vaya correctamente 
    try:
        with sr.Microphone() as source:  # Tomo nuestro microfono como fuente de escuchar cosas 
            print("Escuchando")  # con este print de escuchando es para saber si la computadora nos esta escuchando
            pc = listener.listen(source) # simplemente esta escuchandoa nuestro microfomo como fuente para que nos escuche creamos esta variable pca la cual le asignaremos al listener a nuestro escuchador . que escuche listem entre parentesis el source  que escuche desde la fuente  pero nos falta algo para que nos empiese a reconer la voz y luego la transforme a texto 
            rec = listener.recognize_google(pc, language="es") # creamos una variable llamada rec que sea igual a listener.recognize_google y entre parentesis la variable pc que creamos arriba Y aparte el lenguaje sea español 
            rec = rec.lower() # vamos a ser que nuestra computadora spa que le estamos hablansdo a ella atravez del nombre que nosotros creamos en la variable name  primero tomamos a nuestra variable rec y que rec sea rec.lowe() va aser un metodo que nos va a servir  a tomar nuestro texto y convertirlo a minuscula 
            if name in rec:  # declaramos un if el nombre esta dentro de este texto entonces se hara lo siguiente 
                rec = rec.replace(name, '')  # reemplazamos nuestro nombre por un string vacio 
    except:
        pass
    return rec  # que todo el metodo nos retorne el reconocimiento que acaba de aser nuestro  microfono 

# funcion principal a la cual se llama run_omar
def run_omar():  # creamos una funcion de run_omarllamaremos a la funcion de listem y la funcion de talk 
    while True:  # un while true se utiliza para crear ciclos repetitivos Para que nuestro asistente virtual siga escuchando 
        rec = listen()  # el retorno de rec va ser igual a rec 
        if 'reproduce' in rec:  # la palabra reproduce in rec va aser que haga cosas que si nosotros decimos reproduce entonces hara lo que nosotros le digamos
            music = rec.replace('reproduce', '')  # una variable music lo igualamos rec.replace(la palabra "reproduce" , "" un string vacido )
            print("Reproduciendo " + music)  # que imprima Reprioduciendo por pantalla mas la variable music que seria lo que nosotros le hemos dicho que reprodusca 
            talk("Reproduciendo " + music)  # y con talk que la computadora dira lo que esta dentro de parentesis 
            pywhatkit.playonyt(music) # con esta linea hara que el asistente habra youtube y reproduzca para ello usamos la libreria de pywhakit .playonyt y entre parentesis la variable music lo que queremos que reproduzca , con esta simple linea de codigo nuestro asistente lo que va aser es todo un proceso paera abrir youtube y reproducirr lo que nosotros le hemos dicho que reproduzca 
        elif 'busca' in rec:  # busca reconocimiento del rec = listen() 
            search = rec.replace('busca', '')  # creamos una variable search y vamos a reemplazar la palabra busca en un string vacido 
            wikipedia.set_lang("es")  # nos va a servir que la informacion que se bbusce en wikipedia nos las mustre en español con el parentesis ("es")
            wiki = wikipedia.summary(search, 1) # creamos una variable llamada wiki que va a ser igual a  wikipedia.summary(search, 1) el metodo sumary resumir la informacion que le decimos a nuestro asistente virtual que busque y lo va a resumir primero en search y el 1 va aser la cantidad de oraciones que queremos que el resumen tenga 
            print(search + ": " + wiki) # luego imprimiremos el search lo que queremos que busque : como string y wiki toda la informacion que nos va a traer wikipedia 
            talk(wiki)  # y con el talk hara para que nuestro asistente habla el asistente hable y nos diga toda la informacion 
        elif 'alarma' in rec:  # crearemos un elif y vamos  a usar la palabra alarma y el in rec de reconocimiento 
            num = rec.replace('alarma', '')  # rremplasaremos la palabra de alarma con un string vacido y usamos la variable num ´para almacenar ese valor 
            num = num.strip()  # cortar el strin vacio que se creo en la hora de reemplazxar <- strip si no lo pasamos va a tener un espacio de,mas ejemplo " 8:30"
            print("Alarma activada a las " + num + " horas")  # lo imprimimmos a la consola nos aparecera lo que este en este mensaje 
            talk("Alarma activada a las " + num + " horas")  # llammos a talk y nos lo dira por voz
            while True:  # para hacer que esta alarma depennde del sonido que haga se repita y que este bucle se termine nosotros le demos a una tecla 
                if datetime.datetime.now().strftime('%H:%M') == num: # un if con datetime que es la libreria que descargamos al inicio . datetime . now().strftime ("%H:%M") y lo igualamos a el num / datetime es una libreria que nos ayuda a manejar fechas y horas dento de python  Y de ello activamos el metodo .now Que vamos a tener nuestra fecha y hora de nuestro sistema actualmente , Esa fecha lo transformamos a string con strftime definimos el formato que tenga nuestra hora y eso lo igualamos a num osea cuando la hora local de nuestro sistema sea igual a la hora que nosotros le vamos a decir a nuestro asistente 
                    print("DESPIERTA !!!") # primero le imprimos este mensaje de la linea en el print 
                    mixer.init()  # utilizamos mixer es una libreria de pygame , primero lo iniciamos como mixer.init y luego vamos a cargar nuestro archivo de musica 
                    mixer.music.load("audio.mp3") # con mixer.music.load y entre parentesis vamos a poner nuestro string con nuestro archivo de musica 
                    mixer.music.play() # luego mixer.music.play()  para que se reproduzca la musica de mixer.music.load("audio.mp3") 
                    if keyboard.read_key() == "s":  # vamos a ser un if keyboard la libreria que importamos , . read_key que es para que lea una tecla que si la letra que puso es igual a "s" entonces
                        mixer.music.stop() # que se detenga la musica con esta funcion y que se detenga el bucle while con el
                        break # breaky se dessactiva nuestra alarma 
        elif 'colores' in rec:
            talk("Enseguida")
            colors.capture()
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)  # el metodo call llamar a un comando que nosotros pongamos dentro de parentesis como str 
                    talk(f'abriendo {site}')
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True) # es sheelll es para decirle como si fuera un comando del cmd
                    talk(f'abriendo {file}')
        elif 'escribe' in rec:
            try:
                with open("nota.txt", "a") as f:
                    write(f)
            except FileNotFoundError as e:
                file = open('nota.txt', 'w')
                write(file)

        elif 'fin' in rec:
            talk('Adios!')
            break

def write(f):
    talk("¿Que quieres que escriba")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo puedes Revisarlo")
    sub.Popen("nota.txt", shell=True)

if __name__ == '__main__':  # encridpoint para que la funcion empieze  desde run_omar()
    run_omar()



# encripoint 

