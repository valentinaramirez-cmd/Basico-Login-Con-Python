from Exceptions import DatoInvalidoException, GmailInvalidoException, UsuarioRepetidoException, GmailRepetidoException, ContrasenaInvalidaException
from GestionUsuarioClass import GestionUsuarios
from UsuarioClass import Usuario
import re


usuarios = GestionUsuarios()

def verificarEmail (email): 

    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")

    if not re.fullmatch(pattern, email):
        flag=0
    else:
        flag=1
    
    return flag


def registrarUsuario(): 
    print("\n---------------------")
    print("\n  REGISTRAR USUARIO")
    print("\n---------------------") 

     

    while True: 
        try: 
            print("\nNombre Completo: ") 
            nombreCom= input()

            if not nombreCom: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")


    while True: 
            try: 
                print("\nGmail: ") 
                gmail= input()

                if not gmail: 
                    raise DatoInvalidoException
                else:
                    try: 
                        flag= verificarEmail(gmail)
                        
                        if flag==1 : 
                            try: 
                                flag= usuarios.buscarGmail(gmail)
                                if flag == 0 : 
                                    break
                                else: 
                                    raise GmailRepetidoException
                            except GmailRepetidoException: 
                                print ("Error. El gmail ya ha sido utilizado") 

                        else: 
                            raise GmailInvalidoException 
                    except GmailInvalidoException: 
                        print ("Error. Ingresar un gmail")
        
            except DatoInvalidoException: 
                print("Error. Es obligatorio ingresar un dato.")

    
    while True:
        try: 
            print("\nUsuario: ")
            user= input()

            if not user: 
                raise DatoInvalidoException
            else: 
                try: 
                    flag= usuarios.buscarUsuario(user)
                    print(flag)
                    if flag == 0 : 
                        break
                    else: 
                        raise UsuarioRepetidoException
                except UsuarioRepetidoException: 
                    print("Error. Nombre de Usuario no disponible")
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    
    while True: 
        try: 
            print("\nContraseña(debe contener minimo 8 caracteres y 1 numero): ")
            contrasena= input()
            
            if not contrasena: 
                raise DatoInvalidoException
            else:  
                try:
                    for c in contrasena: 
                        if c.isdigit() == True:
                            aux = 1
                    if aux == 1:  
                            try: 
                                if len(contrasena) >= 8 : 
                                    break
                                else: 
                                    raise ContrasenaInvalidaException
                            except ContrasenaInvalidaException: 
                                print("Error. La contraseña debe tener al menos 8 caracteres. ") 
                    else: 
                        raise ContrasenaInvalidaException
           
                except: 
                    print("Error. La contraseña debe contener al menos 1 numero. ")
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    usuario = Usuario(nombreCom, gmail, user, contrasena)

    usuarios.guardarUsuario(usuario) 

    print("Usuario registrado con exito.")


def iniciarSesion(): 
    print("\n--------------------")
    print("\n   INICIO SESION")
    print("\n--------------------")

    print("\nUsuario: ")
    user= input()

    flag=usuarios.buscarUsuario(user)

    if(flag != 0):
        print("\nContraseña: ")
        contrasena= input() 

        if(contrasena == flag.contrasena): 
            print("\nSesion iniciada. ")
            menuSesionIniciada(flag)
        else: 
             print("\nContraseña incorrecta. ")
    else: 
        print("\nUsuario no existe. ")


    
def menu(): 

    flag=1

    while flag == 1 :
        print("\n--------------------")
        print("\n       MENU")
        print("\n--------------------")
        print("\n[ Ingresar Opcion ] \n\n[1] Iniciar Sesion  \n\n[2] Registrar Usuario  \n\n[3] Visualizar todos los usuarios")
        print("\n--------------------")

        op=int(input())

        if op == 1 : 
            iniciarSesion()
        elif op == 2 : 
            registrarUsuario()
        elif op == 3 : 
            for a in usuarios.listaUsuarios : 
                print (a)
        else : 
            print("\nLa opcion ingresada es incorrecta. Para volver al menu ingresar 1.")
            flag=int(input())


def menuSesionIniciada(us): 
    flag=1

    while flag == 1 :
        print("\n--------------------")
        print("\n    MENU USUARIO")
        print("\n--------------------")
        print("\n[ Ingresar Opcion ] \n\n[1] Visualizar mis datos \n\n[2] Volver al menu principal \n\n[3] Cerrar Sesion ")
        print("\n--------------------")

        op=int(input())

        if op == 1 : 
            print(us)
        elif op == 2 : 
            menu()
        elif op == 3 : 
            flag=0 
        else : 
            print("\nLa opcion ingresada es incorrecta. Para volver al menu ingresar 1.")
            flag=int(input())
    
menu()