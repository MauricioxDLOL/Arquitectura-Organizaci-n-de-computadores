# Lab_1_AOC

## 👥 Autores

**Paralelo 201**
* Javiera Ibaca Morales
* Rol: 202273624-0

**Paralelo 200**
* Rodrigo Ariel Cáceres Gaete
* Rol: 202273616-k

## 📝 Descripción

**Compilación**
Para la correcta compilación de este juego, se recomienda usar Visual Studio Code para abrir el archivo llamado t1.py. Posterior a eso debe compilar el código haciendo click en la opción de 'Run Code' (Simbolo de 'play' en la esquina superior derecha de la ventana de VSC), por consiguiente se abrirá la terminal donde empezará el juego y solamente tendrá que seguir lo indicado en la terminal. Otra opción para compilar el código es simplemente haciendo doble click en el archivo t1.py, así se abrirá una pestaña de cmd donde se podrá jugar, sin embargo esto no es recomendado. 

**Desafío de Conversión y Juego de Tablero**

Este proyecto en Python contiene una colección de funciones que permiten realizar conversiones entre sistemas numéricos (binario, octal, decimal y hexadecimal) y un minijuego que genera un tablero con un desafío final de conversión.

## 🚀 Características

Conversión de:
* Binario a Decimal
* Octal a Decimal
* Hexadecimal a Decimal
* Decimal a Binario, Octal o Hexadecimal

Juego que:
* Genera un tablero aleatorio con un jugador 'S', un objetivo '*' y guardias '!'
* Incluye un desafío final para convertir números desde una base numérica a decimal

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

### 📄 t1.py
* `juego()`: Función principal que inicializa y controla el flujo de juego

## 🧠 Lógica del Desafío

La base numérica utilizada depende del largo del tablero:

| Tamaño del tablero | Sistema numérico |
|--------------------|------------------|
| 0-20               | Binario          |
| 21-100             | Octal            |
| >100               | Hexadecimal      |

El desafío consiste en convertir correctamente un número de la base correspondiente a decimal.

## 🛠️ Requisitos
* Python 3.6 o superior
* Editor recomendado: Visual Studio Code (VSC)
* No requiere librerías externas
