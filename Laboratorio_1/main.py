import random
from conversiones import decimalABinario, binarioADecimal, decimalAOctal, octalADecimal, decimalAHexadecimal, hexadecimalADecimal

def menu():
    print("\n=== Academia de Hackers Éticos CyberSecure ===\n")
    print("1. Generador y Desafío de Códigos de bases a decimal")
    print("2. Generador y Desafío de Códigos de decimal a bases")
    print("3. Salir")
    opcion = input("\nSelecciona una opción: ")
    return opcion

def menu_inicial():
    print("\n=== Academia de Hackers Éticos CyberSecure ===\n")
    print("1. Desafío ByteMaster")
    print("2. Salir")
    opcion = input("\nSelecciona una opción: ")
    return opcion


def generador_codigos():
    print("\n--- Generador de Códigos de Acceso ---\n")
    print("firewall  → Binario (1-63)")
    print("servidor  → Octal (1-511)")
    print("memoria   → Hexadecimal (1-4095)")
    sistema = input("\n¿Qué sistema quieres hackear? (firewall/servidor/memoria): ").strip().lower()
    if sistema not in ["firewall", "servidor", "memoria"]:
        print("Sistema no válido. Intenta de nuevo.")
        return False
    desbloqueo_mostrado = False
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
                        desbloqueo_mostrado = True
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
                        desbloqueo_mostrado = True
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
                        desbloqueo_mostrado = True
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

def desafio_descifrado():
    print("\n--- Desafío de Descifrado ---\n")
    print("Elige el tipo de código a descifrar:")
    print("1. Binario a Decimal")
    print("2. Octal a Decimal")
    print("3. Hexadecimal a Decimal")
    opcion = input("Opción: ").strip()
    correcto = False
    if opcion == "1":
        numero = random.randint(1, 63)
        codigo = decimalABinario(numero)
        print(f"Código en binario: {codigo}")
        intento = input("¿Cuál es el valor decimal?: ")
        try:
            if int(intento) == binarioADecimal(codigo):
                print("¡Correcto! Avanzas de nivel.")
                correcto = True
            else:
                print(f"Incorrecto. El valor era {numero}.")
        except:
            print("Entrada inválida.")
    elif opcion == "2":
        numero = random.randint(1, 511)
        codigo = decimalAOctal(numero)
        print(f"Código en octal: {codigo}")
        intento = input("¿Cuál es el valor decimal?: ")
        try:
            if int(intento) == octalADecimal(codigo):
                print("¡Correcto! Avanzas de nivel.")
                correcto = True
            else:
                print(f"Incorrecto. El valor era {numero}.")
        except:
            print("Entrada inválida.")
    elif opcion == "3":
        numero = random.randint(1, 4095)
        codigo = decimalAHexadecimal(numero)
        print(f"Código en hexadecimal: {codigo}")
        intento = input("¿Cuál es el valor decimal?: ")
        try:
            if int(intento) == hexadecimalADecimal(codigo):
                print("¡Correcto! Avanzas de nivel.")
                correcto = True
            else:
                print(f"Incorrecto. El valor era {numero}.")
        except:
            print("Entrada inválida.")
    else:
        print("Opción no válida.")
    return correcto

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
