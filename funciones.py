import random
import string

#  Creamos una funcion para crear contraseñas de manera aleatoria con mayusculas, minusculas y numeros.
def passwoord_create(lenght):
    characters = string.ascii_letters+string.digits
    password = ""
    for i in range(lenght):
        password += characters[random.randint(0,len(characters)-1)]
    return password

# Creamos un removedor de tildes para el nombre de los usuarios
def remove_accents(name_string):
    accents = name_string
    accents = accents.replace("á", "a") 
    accents = accents.replace("é", "e")
    accents = accents.replace("í", "i")
    accents = accents.replace("ó", "o")
    accents = accents.replace("ú", "u")
    return accents

# Creamos funcion para crear cuentas de usuarios
def user_create(nombre, edad):
    username = remove_accents(nombre[0:4].lower()) + remove_accents(nombre[nombre.index(" ")+1:-3].lower().replace(" ","_"))+str(edad)
    return username

# Crearemos funcion para crear la cuenta para el usuario
def generate_account(users):
    account = []
    for user in users:
        element = {
            "Cuenta": user_create(user["nombre"], user["edad"]),
            # Asignaremos una contraseña a la cuenta
            "Contraseña": passwoord_create(10)
        }
        account.append(element)
        return account
    
# Creamos funcion para pedir al usuario ingresar su numero de telefono
def phone_number(users):
    for user in users:
        while True:
            phone = input(user["nombre"]+", por favor, ingrese su numero numero de telefono de 8 digitos: ")
            # Mediante lo siguiente verificamos que el numero de telefono contenga 8 digitos
            if len(phone) == 8 and phone.isnumeric():
                user["telefono"] = phone
            else:
                print("\n\nSu numero de telefono debe tener solo 8 digitos, intentelo nuevamente.\n")
    return users
