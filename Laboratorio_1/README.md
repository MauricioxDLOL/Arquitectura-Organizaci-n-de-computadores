# Lab_1_AOC

## 👥 Autores

**Paralelo 200**
* Javiera Ibaca Morales
* Rol: 202273624-0

**Paralelo 200**
* 
* Rol: 

## 📝 Descripción

**Compilación**


## 🚀 Características

Conversión de:
* Binario a Decimal
* Octal a Decimal
* Hexadecimal a Decimal
* Decimal a Binario, Octal o Hexadecimal

## 📁 Estructura del Código

📁 Estructura del Código
  > 📄 generación_escenario.py  # Generación y visualización del tablero  
  > 📄 conversiones.py          # Funciones de conversión entre sistemas numéricos  
  > 📄 logica_movimiento.py     # Manejo del movimiento de jugador y guardias  
  > 📄 t1.py                 # Función principal y punto de entrada  

## Módulos y Funciones

### 📄 generación_escenario.py
* `generar_tablero()`: Crea el escenario de juego
* `mostrar_tablero()`: Visualiza el tablero en consola
* `validar_entrada()`: Verifica la entrada del usuario

### 📄 logica_movimiento.py
* `mover_jugador()`: Controla el movimiento del personaje principal
* `mover_guardias()`: Gestiona el comportamiento de los guardias

### 📄 conversiones.py
* `convertir_binario_a_decimal()`: Traduce números binarios a decimales
* `convertir_octal_a_decimal()`: Traduce números octales a decimales
* `convertir_hexadecimal_a_decimal()`: Traduce números hexadecimales a decimales
* `convertir_a_binario(numero)`: Convierte decimales a binario
* `convertir_a_octal(numero)`: Convierte decimales a octal
* `convertir_a_hexadecimal(numero)`: Convierte decimales a hexadecimal
* `convertir_a_decimal(largo)`: Determina la base según el tamaño del tablero
* `desafio_conversion(largo)`: Genera el reto de conversión final

El desafío consiste en convertir correctamente un número de la base correspondiente a decimal.

## 🛠️ Requisitos
* Python 3.6 o superior
* Editor recomendado: Visual Studio Code (VSC)
* No requiere librerías externas
