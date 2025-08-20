# CONVERSIONES DE BASES

def decimalABinario(numero):
    binario = ''

    while(numero >= 1):
        binario+= str(int(numero % 2))
        numero/=2

    return int(binario[::-1])


def binarioADecimal(numero):
    suma = 0

    for i, valor in enumerate(str(numero)[::-1]):

        suma+= int(valor)*(2**i)
       
    return suma


def decimalAOctal(numero):
    octal = ''

    while(numero >= 1):
        octal+= str(int(numero % 8))
        numero/=8

    return int(octal[::-1])

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

