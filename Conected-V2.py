from Funciones_de_conected import *
import os

mostrar_bienvenida()
nombre = obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
if existe_archivo(nombre+".user"):
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento, amigos,muro) = usuario_existente(nombre)
else:
    print('---> !Al parecer eres un usuario nuevo, así que hagamos tu nuevo perfil en CONNECTED¡ <---')
    print()
    (nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais,  instrumento, amigos) = obtener_datos()
    muro = []
    print()
# Ahora mostramos los datos ingresados por el usuario.
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos que ingresaste.")
mostrar_perfil(nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento, amigos)
print("Gracias por la información ingresada, recuerda que puedes modificarla cuando gustes")
print("Ahora ya puedes disfrutar de CONNECTED")
print("--------------------------------------------------")
# ingresamos al menu de opciones.
opcion = 8
while opcion != 0:
    opcion = opcion_menu_1()
    if opcion == 1:
        mensaje = obtener_mensaje()
        publicar_mensaje(nombre,amigos,mensaje,muro)
    elif opcion == 2:
        for i in range(len(amigos)):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mensaje = obtener_mensaje()
            mostrar_mensaje(nombre, nombre_amigo, mensaje)
    elif opcion == 3:
        mostrar_muro(muro)
    elif opcion == 4:
        opcion = 7
        while opcion != 8:
            opcion = menu_actualizar_datos()
            if opcion == 1:
                nombre = obtener_nombre()
                print('¡Tu nombre se ha actualizado con éxito!')
            elif opcion == 2:
                email = obtener_email()
                print('¡Tu e-mail se ha actualizado con éxito!')
            elif opcion == 3:
                telefono = obtener_telefono()
                print('¡Tu teléfono se ha actualizado con éxito!')
            elif opcion == 4:
                pais = obtener_pais()
                print('¡Tu país se ha actualizado con éxito!')
            elif opcion == 5:
                instrumento = obtener_instrumento()
                print('¡Tu(s) instrumento(s) se ha actualizado con éxito!')
            elif opcion == 6:
                accion = menu_amigos()
                if accion == 1:
                    amigos = obtener_lista_amigos()
                elif accion == 2:
                    na = amigo_nuevo()
                    amigos = agregar_amigo(amigos, na)
                print('¡Tu lista de amigos se ha actualizado con éxito!')
            elif opcion == 7:
                agno = obtener_edad()
                print('¡Tu año de nacimiento se ha actualizado con éxito!')
            elif opcion == 0:
                opcion = 8
            print('___________________________________________________')
            print('Datos Actualizados:')
            mostrar_perfil(nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento, amigos)
            print()
    elif opcion == 5:
        mostrar_perfil(nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento, amigos)
        print()
    elif opcion == 6:
        cambiar_de_usuario()
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre + ".user")
        guardar_datos_usuario_n(nombre, edad, sexo, estatura_m, estatura_cm, email, telefono, pais, instrumento, amigos,muro)
        print("Archivo", nombre + ".user", "guardado")

print()
# Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Connected. ¡Hasta pronto!")
