# Lab_1_AOC

## 👥 Autores

**Paralelo 200**
* Javiera Ibaca Morales
* Rol: 202273624-0

**Paralelo 200**
* Mauricio Godoy Cárcamo
* Rol: 202304014-2

## 📝 Descripción

Simulador de entrenamiento de hacking ético donde el usuario debe dominar las conversiones entre diferentes bases numéricas utilizadas en sistemas de seguridad informática. El programa presenta dos modos de juego:

1. **Generador de códigos:** El usuario debe descifrar códigos en binario, octal o hexadecimal y convertirlos a decimal para avanzar de nivel.
2. **Desafío de descifrado:** Una vez superado el primer desafío, se sube de nivel y se desbloquea el modo para convertir números decimales a binario, octal o hexadecimal. (mecánica añadida por criterio de los programadores :) )

El objetivo es practicar y dominar las conversiones manuales entre bases, sin usar funciones automáticas de Python.

## Características

- Conversión de binario, octal y hexadecimal a decimal.
- Conversión de decimal a binario, octal y hexadecimal.
- Menú interactivo y validación de entradas.
- Mensajes de avance y desbloqueo de modos.

## Estructura del Código

- `main.py`: Archivo principal, contiene el menú y la lógica de los modos de juego.
- `conversiones.py`: Funciones de conversión entre sistemas numéricos (todas implementadas manualmente).

## Algoritmos y Desarrollo

**Algoritmos de conversión:**
- Binario/Octal/Hexadecimal a Decimal: Se recorre el string de la base elegida y se multiplica cada dígito por la potencia correspondiente.
- Decimal a Binario/Octal/Hexadecimal: Se divide sucesivamente el número entre la base y se almacenan los restos.

**Desarrollo:**
- No se utiliza ninguna función automática de conversión de Python (`bin()`, `oct()`, `hex()`, `int(x, base)`, etc.).
- El usuario puede elegir el sistema a hackear y debe ingresar la conversión correcta para avanzar.
- El menú para navegar entre conversiones se desbloquea solo tras superar el primer desafío (por default de bases a decimal).

## 💡 Supuestos

- El usuario conoce las reglas básicas de conversión entre bases.
- El usuario ingresa solo números válidos y selecciona opciones del menú correctamente.
- El programa está diseñado para uso educativo y no requiere librerías externas.

## ▶️ Ejecución

1. Ejecuta `main.py` con Python 3.6 o superior.
2. Sigue las instrucciones en pantalla para elegir el modo de juego y realizar las conversiones.
3. Al superar el primer desafío, se desbloquean ambos modos de conversión.

## 🛠️ Requisitos

- Python 3.6 o superior
- Editor recomendado: Visual Studio Code (VSC)
- No requiere librerías externas
