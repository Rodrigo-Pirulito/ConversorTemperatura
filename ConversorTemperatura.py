while True:
    celsius = input("Qual a temperatura em celsius você deseja converter?")
    try:
        verificador = float(celsius)
        break
    except ValueError:
        print("***Resposta inapropriada***\n")

while True:
    modo = input("\n Converter para fahrenheit ou kelvin?\n1=fahrenheit\n2=kelvin\n\t")
    try:
        if float(modo) == 1:
            fahrenheit = float(celsius)*1.8 + 32
            print(f"\nVocê detem {fahrenheit}° fahrenheit")
            break
        if float(modo) == 2:
            kelvin = float(celsius)+273,15
            print(f"\nVocê detem {kelvin}° kelvin")
            break
    except ValueError:
        print("***Resposta inapropriada***\n")
