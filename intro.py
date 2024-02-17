# juliana quiere ir a china pero no money, solo 100 EUR. Tiene novio y amiguito. 
# Mando una noche un estado diciendo que quiere ir a china. 
# El grupo de fans le contesta vamos, pero juliana solo quiere money para irse sola. 
# El amiguito le plantea que tiene 500 EUR, pidiendo prestado 1000 EUR a la madre para un total 1500 para que se vaya ella. Juliana dice que 1200 necesita para irse.


option1 = {
    "Name": "No viajar",
    "TotalGastos": 0,
    "TotalDeuda": 0
}

option2 = {
    "Name": "Paquete de 3 días en China",
    "Tickets": 250,
    "Hotel": 200,
    "Food": 100,
    "Activities": 50,
    "TotalGastos": 600,
    "TotalDeuda": 500
}

option3 = {
    "Name": "Paquete de 7 días en China",
    "Tickets": 250,
    "Hotel": 400,
    "Food": 250,
    "Activities": 150,
    "Extra tour": 150,
    "Souvenirs": 400,
    "TotalGastos": 1600,
    "TotalDeuda": 1500
}

def getPlan(option):
    print("Este sería tu plan: ")
    if (option == 1):
        print(option1)
        print("------------------------------------------------------")
    elif (option == 2):
        print(option2)
        print("------------------------------------------------------")
    elif (option == 3):
        print(option3)
        print("------------------------------------------------------")
    elif (option == 4):
        print("FIN")
        print("------------------------------------------------------")
    else:
        print("Opción no válida")
        print("------------------------------------------------------")


userOption = 0

while userOption != 4:
    print("Ingrese la opcion de acuerdo a su presupuesto: ")
    print("1. Tengo menos de 600 EUR")
    print("2. Tengo 600 EUR")
    print("3. Tengo 1600 EUR")
    print("4. Salir del programa")
    userOption = int(input("Tu selección: "))

    getPlan(userOption)


   