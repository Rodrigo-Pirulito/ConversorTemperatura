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
            celsius = float(celsius)*33.8
            print(f"\nVocê detem {celsius}")
            break
    except ValueError:
        print("***Resposta inapropriada***\n")
