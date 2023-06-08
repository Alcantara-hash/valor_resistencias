#Funciones
def comprobar_bandas():
    bandas = {
        "Negro": "0",
        "Cafe": "1",
        "Rojo": "2",
        "Naranja": "3",
        "Amarillo": "4",
        "Verde": "5",
        "Azul": "6",
        "Violeta": "7",
        "Gris": "8",
        "Blanco": "9"
    }

    while True:

        color1 = input("Ingrese el primer color: ").capitalize()
        color2 = input("Ingrese el segundo color: ").capitalize()

        if color1 in bandas and color2 in bandas:
            valor_color1= bandas[color1]
            valor_color2= bandas[color2]
            break
        else:
            print("Uno o ambos colores no son válidos. Intente nuevamente.")

    return color1, color2, valor_color1, valor_color2

def comprobar_multiplicador():
    multiplicador= {
    "Negro": [1, "Ω"],
    "Cafe":[10, "Ω"],
    "Rojo":[100, "Ω"],
    "Naranja":[1, "KΩ"],
    "Amarillo":[10, "KΩ"],
    "Verde":[100, "KΩ"],
    "Azul":[1, "MΩ"],
    "Violeta":[10, "MΩ"],
    "Gris":[100, "MΩ"],
    "Blanco":[1, "GΩ"],
    "Oro":[0.1, "Ω"],
    "Plata":[0.01, "Ω"]
    }

    while True:
        color = input("Ingresa el tercer color: ").capitalize()

        if color in multiplicador:
            valor_tercer_color= multiplicador[color][0]
            equivalencia= multiplicador[color][1]
            break
        else:
            print("El color ingresado no es valido. Intente nuevamente.")
        
    return color, valor_tercer_color, equivalencia

def comprobar_tolerancia():
    tolerancia= {
    "Cafe":1,
    "Rojo":2,
    "Verde":0.5,
    "Azul":0.25,
    "Violeta":0.10,
    "Gris":0.05,
    "Oro":5,
    "Plata":10
    }

    while True:
        color = input("Ingresa el cuarto color: ").capitalize()

        if color in tolerancia:
            porcentaje= tolerancia[color]
            break
        else:
            print("El color ingresado no es válido. Intente nuevamente.")
        
    return color, porcentaje

def determinarValor():
    resultado_uno= (int(valor_primer_color+valor_segundo_color))*valor_tercer_color
    resultado_dos= resultado_uno+((porcentaje_color*resultado_uno)/100)
    resultado_tres= resultado_uno-((porcentaje_color*resultado_uno)/100)
    return resultado_uno, resultado_dos, resultado_tres



# Main

repetir= True
while repetir:

    print("\n###### Calculo del valor de una resistencia ######\n")
    
    confirmacion= True
    while confirmacion:
        primer_color, segundo_color, valor_primer_color, valor_segundo_color = comprobar_bandas()
        tercer_color, valor_tercer_color, equivalencia_final = comprobar_multiplicador()
        cuarto_color, porcentaje_color = comprobar_tolerancia()

        print("\nTu resistencia es: ")
        print(f"Color 1: {primer_color}\nColor 2: {segundo_color}\nColor 3: {tercer_color}\nColor 4: {cuarto_color}")

        confirmacion= int(input("Para continuar el proceso ingrese '0', para re-escribir los colores ingrese '1'.\nOpcion: "))

    print("\n\n###### Resultados ######")
    res_uno, res_dos, res_tres= determinarValor()
    print(f"{round(res_uno, 2)} {equivalencia_final} +|- {porcentaje_color}%")
    print("ó")
    print(f"{round(res_dos, 2)} {equivalencia_final} <-> {round(res_tres, 2)} {equivalencia_final}\n")

    repetir= int(input(" - Para SALIR ingrese '0', para realizar un NUEVO CALCULO ingrese '1'.\nOpcion: "))

    if repetir == 0:
        print("\n!Hasta luego¡")