# En este módulo se encuentran las funciones para el programa de mi red social (conected)
import os


def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""                                   __             .___
      ____  ____   ____   ____   _____/  |_  ____   __| _/
    _/ ___\/  _ \ /    \_/ __ \_/ ___\   __\/ __ \ / __ | 
    \  \__(  <_> )   |  \  ___/\  \___|  | \  ___// /_/ | 
     \___  >____/|___|  /\___  >\___  >__|  \___  >____ | 
         \/           \/     \/     \/          \/     \/

    """)
    print("Donde podrás compartir con tus contactos tus creaciones musicales")

# Obtener nombre.
def obtener_nombre():
    nombre = input("Dime, como te llamas. -> ")
    while nombre == '':
        print('Escribe tu nombre para continuar')
        nombre = input('¿cómo te llamas? ->')
    return nombre


# Obtener año de nacimiento y calcular edad.
def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste.-> "))
    while agno < 1930 or agno > 2022:
        print('ingresa tu año de nacimiento correctamente...')
        agno = input('en qué año naciste?')
    edad = 2022 - agno - 1
    return edad


# Obtener sexo.
def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo


# Obtener e-mail del usuario.
def obtener_email():
    email = input("También necesitamos tener tu correo electrónico, por favor, escríbelo aqui -> ")
    while email == '':
        print('Por favor, es necesario llenar este campo')
        email = (input('También necesitamos tener tu correo electrónico, por favor, escríbelo aqui -> '))
    return email


# Obtener número telefónico del usuario.
def obtener_telefono():
    telefono = input(str("cuál es tu número telefónico, recuerda incluir el código de tu país ->"))
    while telefono == '':
        print('Es necesario llenar este campo para continuar')
        telefono = input(str('Ingresa tu número telefónico, recuerda incluir el código de tu país ->'))
    return telefono


# Obtener nacionalidad del usuario.
def obtener_pais():
    pais = input("¿En que país vives? ->")
    while pais == '':
        print('Es necesario llenar este campo para continuar')
        pais = input('¿En que país vives?')
    return pais


# Obtener instrumento musical que toca el usuario.
def obtener_instrumento():
    instrumento = (input("Cuéntanos cuales instrumento musicales tocas, separados por una coma(,) ->"))
    if instrumento == '':
        instrumento = 'Ninguno'
    else:
        instrumento = instrumento
    return instrumento


# Obtener la estatura del usuario.
def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. cuánto mides? Dímelo en metros. -> "))
    metro = int(estatura)
    centimetro = int((estatura - metro) * 100)
    return (metro, centimetro)


# Obtener la cantidad de amigos del usuario.
def obtener_lista_amigos():
    linea = str(input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': "))
    amigos = linea.split(",")
    return amigos

# Solicitar todos los datos dentro de una función.
def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    s = obtener_sexo()
    (mt, cm) = obtener_estatura()
    em = obtener_email()
    t = obtener_telefono()
    p = obtener_pais()
    ins = obtener_instrumento()
    la = obtener_lista_amigos()
    return (n,e,s,mt,cm,em,t,p,ins,la)


# Esta función muestra el perfil con los datos ingresados por el usuario.
def mostrar_perfil(nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento, amigos):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("sexo, ", sexo)
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("email, ", email)
    print("teléfono, ", telefono)
    print("pais donde vives, ", pais)
    print("instrumento(s) que toca(s), ", instrumento)
    print("Cantidad de amigos:  ", len(amigos))
    print("Tus amigos son:", amigos)
    print("--------------------------------------------------")

# Funcion para desplegar el menu principal.
def opcion_menu_1():
    print('¿Qué deseas hacer?:')
    print('1-. Escribir un mensaje público')
    print('2-. Escribir mensaje solo amigos')
    print('3-. Mostrar muro')
    print('4-. Actualizar tus datos')
    print("4-. mostrar datos del usuario")
    print('6-. Cambiar de Usuario')
    print('0-. Salir')
    print()
    opcion = int(input('Ingresa el numero de la opción que deseas realizar aquí ->'))
    while opcion < 0 or opcion > 6:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

# Función para obtener el mensaje público.
def obtener_mensaje():
    mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    print(origen, destinatario, mensaje)
    print("--------------------------------------------------")

#Muestra los mensajes recibidos
def mostrar_muro(muro):
     print("------ MURO ("+str(len(muro))+" mensajes) ---------")
     for mensaje in muro:
         print(mensaje)
     print("--------------------------------------------------")

#Publica un mensaje en el timeline personal y en el de los amigos
def publicar_mensaje(origen, amigos, mensaje, muro):
    print("--------------------------------------------------")
    print(origen, "dice:", mensaje)
    print("--------------------------------------------------")
    #Agrega el mensaje al final del timeline local
    muro.append(mensaje)
    #Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user","a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close()


#funcion para actualizar datos. Esta tiene un menú integrado
def menu_actualizar_datos():
        print('¿Qué datos deseas actualizar?')
        print('1-. Nombre')
        print('2-. E-mail')
        print('3-. Número de teléfono')
        print('4-. país donde vives')
        print('5-. Instrumento musical')
        print('6-. Lista de amigos')
        print('7-. Edad')
        print('0-. Ir al menú anterior')
        print()
        opcion = int(input('Ingresa el numero de la opción que deseas realizar aquí ->'))
        print()
        while opcion < 0 or opcion > 7:
            print("No conozco la opción que has ingresado. Inténtalo otra vez.")
            opcion = int(input("Ingresa una opción: "))
        return opcion

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def usuario_existente(nombre):
    archivo_usuario = open(nombre+'.user','r')
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    sexo = archivo_usuario.readline().rstrip()
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m)*100)
    email = archivo_usuario.readline().rstrip()
    telefono = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    instrumento = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    # Una vez que hemos leído los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return (nombre,edad,sexo,estatura_m,estatura_cm,email,telefono,pais,instrumento,amigos,muro,)

def guardar_datos_usuario_n(nombre,edad,sexo,estatura_m,estatura_cm,email,telefono,pais,instrumento,amigos,muro):
    archivo_usuario = open(nombre + '.user', 'w')
    archivo_usuario.write(nombre + "\n")
    archivo_usuario.write(str(edad) + "\n")
    archivo_usuario.write(sexo + "\n")
    archivo_usuario.write(str(estatura_m + estatura_cm / 100) + "\n")
    archivo_usuario.write(str(email + "\n"))
    archivo_usuario.write(str(telefono + "\n"))
    archivo_usuario.write(pais + "\n")
    archivo_usuario.write(instrumento + "\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    archivo_usuario.close()

def cambiar_de_usuario():
    nombre = input('¿A qué perfil deseas cambiar?')
    if existe_archivo(nombre + '.user'):
        (nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento,amigos,muro) = usuario_existente(nombre)
        mostrar_perfil(nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento,amigos)
    else:
        print('No se Puede cambiar de Usuario')

def amigo_nuevo():
    na = str(input('Ingresa el nombre de tu nuevo amigo:  '))
    return na

def agregar_amigo(amigos, amigo_nuevo):
    amigos.append(amigo_nuevo)
    return amigos


def menu_amigos():
    print('________________________________________________________')
    print('1-. Actualizar Toda la Lista de amigos')
    print('2-. Agregar un nuevo amigo')
    accion = int(input('ingresa la acción que deseas realizar:  '))
    print('________________________________________________________')
    return accion