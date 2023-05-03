from funciones import phone_number, generate_account

# Mensaje de bienvenida
bienvenida = "=-="*13+"\n| Bienvenido a «Yo quiero otro mundo» |\n"+"=-="*13+"\n"
print(bienvenida)

# Lista de Usuarios
users = [
    {
        "nombre": "Felipe Flores",
        "edad": 35,
        "genero": "Masculino",
        "direccion": "Baquedano 334",
    },
    {
        "nombre": "Brayan Valtierra",
        "edad": 42,
        "genero": "Masculino",
        "direccion": "Baquedano 337",
    },
    {
        "nombre": "Claudio Meza",
        "edad": 34,
        "genero": "Masculino",
        "direccion": "Baquedano 442",
    },
    {
        "nombre": "Martin Meza",
        "edad": 33,
        "genero": "Masculino",
        "direccion": "Baquedano 332",
    },
    {
        "nombre": "Ignacio Muñoz",
        "edad": 35,
        "genero": "Masculino",
        "direccion": "Baquedano 420",
    },
    {
        "nombre": "Yarlette Carmona",
        "edad": 44,
        "genero": "Femenino",
        "direccion": "Baquedano 425",
    },
    {
        "nombre": "Emma Calderón",
        "edad": 20,
        "genero": "Femenino",
        "direccion": "Baquedano 422",
    },
    {
        "nombre": "Romina Chavez",
        "edad": 28,
        "genero": "Femenino",
        "direccion": "Baquedano 391",
    },
    {
        "nombre": "Felipe Canales",
        "edad": 45,
        "genero": "Masculino",
        "direccion": "Baquedano 395",
    },
    {
        "nombre": "Nicolás Calderón",
        "edad": 43,
        "genero": "Masculino",
        "direccion": "Baquedano 398",
    },
]

# Elaboramos que recorra una lista de 10 usuarios mediante un print llamando el nombre de la lista
print("/// Lista de usuarios ///")
print(users)
print("\n"+"=-="*20+"\n")

# cada cuenta debera guardarse con un atributo nuevo
access = generate_account(users)
print(access)
print("\n")

phones = phone_number(users)
print(users)
print("=-="*20+"\n")