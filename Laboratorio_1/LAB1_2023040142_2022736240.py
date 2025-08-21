import random

# CONVERSIONES DE BASES


# Convierte un número decimal a binario 
def decimalABinario(numero):
    binario = ''

    while(numero >= 1):
        binario+= str(int(numero % 2))
        numero/=2

    return int(binario[::-1])


# Convierte un número binario a decimal 
def binarioADecimal(numero):
    suma = 0

    for i, valor in enumerate(str(numero)[::-1]):

        suma+= int(valor)*(2**i)
       
    return suma

# Convierte un número decimal a octal (como string)

def decimalAOctal(numero):
    octal = ''

    while(numero >= 1):
        octal+= str(int(numero % 8))
        numero/=8

    return int(octal[::-1])


# Convierte un número octal a decimal 

def octalADecimal(numero):
    suma = 0

    for i, valor in enumerate(str(numero)[::-1]):
        suma+= int(valor)*(8**i)
    
    return suma

# Convierte un número decimal a hexadecimal (como string)
def decimalAHexadecimal(numero):
    hexadecimal = ''
    hex_chars = '0123456789ABCDEF'
    while numero >= 1:
        hexadecimal += hex_chars[int(numero % 16)]
        numero //= 16
    return hexadecimal[::-1]

# Convierte un número hexadecimal (como string) a decimal
def hexadecimalADecimal(numero):
    suma = 0
    hex_chars = '0123456789ABCDEF'
    numero = numero.upper()
    for i, valor in enumerate(numero[::-1]):
        suma += hex_chars.index(valor) * (16 ** i)
    return suma


# Menú cuando se sube de nivel
def menu():
    print("\n=== Academia de Hackers Éticos CyberSecure ===\n")
    print("1. Generador y Desafío de Códigos de bases a decimal")
    print("2. Generador y Desafío de Códigos de decimal a bases")
    print("3. Salir")
    opcion = input("\nSelecciona una opción: ")
    return opcion

#Menu inicial
def menu_inicial():
    print("\n=== Academia de Hackers Éticos CyberSecure ===\n")
    print("1. Desafío ByteMaster")
    print("2. Salir")
    opcion = input("\nSelecciona una opción: ")
    return opcion


# Menu para seleccionar la opción de conversión

def generador_codigos():
    print("\n--- Generador de Códigos de Acceso ---\n")
    print("firewall  → Binario (1-63)")
    print("servidor  → Octal (1-511)")
    print("memoria   → Hexadecimal (1-4095)")
    sistema = input("\n¿Qué sistema quieres hackear? (firewall/servidor/memoria): ").strip().lower()
    if sistema not in ["firewall", "servidor", "memoria"]:
        print("Sistema no válido. Intenta de nuevo.")
        return False
    
    primer_acierto = True
    while True:
        if sistema == "firewall":
            numero = random.randint(1, 63)
            codigo = decimalABinario(numero)
            print("\n--- Desafío de descifrado ---\n")
            print(f"Código en binario: {codigo}")
            intento = input("¿Cuál es el valor decimal?: ")
            try:
                if int(intento) == binarioADecimal(codigo):
                    if primer_acierto:
                        print("¡Correcto! Avanzas de nivel.")
                        print("\n¡Felicidades! Has desbloqueado las conversiones de bases a decimal y decimal a binario/octal/hexadecimal. ¡Sigue hackeando!\n")
                        
                        primer_acierto = False
                    else:
                        print(random.choice(["\n¡Correcto!\n", "\n¡Bien hecho!\n", "\n¡Excelente!\n"]))
                    reintentar = input("¿Quieres volver a intentarlo? (s/n): ").strip().lower()
                    if reintentar == 's':
                        continue
                    return True
                else:
                    print(f"\nHa fallado el hackeo. El valor era {numero}.")
            except:
                print("Entrada inválida.")
        elif sistema == "servidor":
            numero = random.randint(1, 511)
            codigo = decimalAOctal(numero)
            print("\n--- Desafío de descifrado ---\n")
            print(f"Código en octal: {codigo}")
            intento = input("¿Cuál es el valor decimal?: ")
            try:
                if int(intento) == octalADecimal(codigo):
                    if primer_acierto:
                        print("¡Correcto! Avanzas de nivel.")
                        print("\n¡Felicidades! Has desbloqueado las conversiones de bases a decimal y decimal a binario/octal/hexadecimal. ¡Sigue hackeando!\n")
                       
                        primer_acierto = False
                    else:
                        print(random.choice(["\n¡Correcto!\n", "\n¡Bien hecho!\n", "\n¡Excelente!\n"]))
                    reintentar = input("¿Quieres volver a intentarlo? (s/n): ").strip().lower()
                    if reintentar == 's':
                        continue
                    return True
                else:
                    print(f"\nHa fallado el hackeo. El valor era {numero}.")
            except:
                print("Entrada inválida.")
        elif sistema == "memoria":
            numero = random.randint(1, 4095)
            codigo = decimalAHexadecimal(numero)
            print("\n--- Desafío de descifrado ---\n")
            print(f"Código en hexadecimal: {codigo}")
            intento = input("¿Cuál es el valor decimal?: ")
            try:
                if int(intento) == hexadecimalADecimal(codigo):
                    if primer_acierto:
                        print("¡Correcto! Avanzas de nivel.")
                        print("\n¡Felicidades! Has desbloqueado las conversiones de bases a decimal y decimal a binario/octal/hexadecimal. ¡Sigue hackeando!\n")
                
                        primer_acierto = False
                    else:
                        print(random.choice(["\n¡Correcto!\n", "\n¡Bien hecho!\n", "\n¡Excelente!\n"]))
                    reintentar = input("¿Quieres volver a intentarlo? (s/n): ").strip().lower()
                    if reintentar == 's':
                        continue
                    return True
                else:
                    print(f"\nHa fallado el hackeo. El valor era {numero}.")
            except:
                print("Entrada inválida.")
        reintentar = input("¿Quieres volver a intentarlo? (s/n): ").strip().lower()
        if reintentar != 's':
            return False


def main():
    primer_nivel_superado = False
    while True:
        if not primer_nivel_superado:
            opcion = menu_inicial()
            if opcion == "1":
                if generador_codigos():
                    print("\n¡Felicidades! Has desbloqueado las conversiones de bases a decimal y decimal a binario/octal/hexadecimal. ¡Sigue hackeando!\n")
                    primer_nivel_superado = True
            elif opcion == "2":
                print("¡Hasta luego, hacker!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        else:
            opcion = menu()
            if opcion == "1":
                generador_codigos()
            elif opcion == "2":
                # Generador de decimal a base
                print("\n--- Generador de Códigos de Decimal a Base ---\n")
                print("firewall  → Binario (1-63)")
                print("servidor  → Octal (1-511)")
                print("memoria   → Hexadecimal (1-4095)")
                sistema = input("\n¿Qué sistema quieres hackear? (firewall/servidor/memoria): ").strip().lower()
                if sistema not in ["firewall", "servidor", "memoria"]:
                    print("Sistema no válido. Intenta de nuevo.")
                    continue
                while True:
                    if sistema == "firewall":
                        numero = random.randint(1, 63)
                        print(f"\nNúmero decimal: {numero}")
                        intento = input("¿Cuál es el valor en binario?: ")
                        try:
                            if intento == str(decimalABinario(numero)):
                                print("¡Correcto! Avanzas de nivel.")
                            else:
                                print(f"\nHa fallado el hackeo. El valor era {decimalABinario(numero)}.")
                        except:
                            print("Entrada inválida.")
                    elif sistema == "servidor":
                        numero = random.randint(1, 511)
                        print(f"\nNúmero decimal: {numero}")
                        intento = input("¿Cuál es el valor en octal?: ")
                        try:
                            if intento == str(decimalAOctal(numero)):
                                print("¡Correcto! Avanzas de nivel.")
                            else:
                                print(f"\nHa fallado el hackeo. El valor era {decimalAOctal(numero)}.")
                        except:
                            print("Entrada inválida.")
                    elif sistema == "memoria":
                        numero = random.randint(1, 4095)
                        print(f"\nNúmero decimal: {numero}")
                        intento = input("¿Cuál es el valor en hexadecimal?: ")
                        try:
                            if intento.upper() == decimalAHexadecimal(numero):
                                print("¡Correcto! Avanzas de nivel.")
                            else:
                                print(f"\nHa fallado el hackeo. El valor era {decimalAHexadecimal(numero)}.")
                        except:
                            print("Entrada inválida.")
                    reintentar = input("¿Quieres volver a intentarlo? (s/n): ").strip().lower()
                    if reintentar != 's':
                        break
            elif opcion == "3":
                print("¡Hasta luego, hacker!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
