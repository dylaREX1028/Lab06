# Lab06
- Universidad de Costa Rica
- Facultad de Ingeniería
- Escuela de Ingeniería Eléctrica
- IE-0117 - Programación Bajo Plataformas Abiertas
- II ciclo 2023
- Laboratorio 06: Funciones Lambda y Callbacks Python
- Participantes:
  - Dilana Rodríguez Jiménez (Carne C06660)
- Profesora: Carolina Trejos
- Fecha: 2 de Diciembre del 2023

## Calculadora
La finalidad de laboratorio es una calculadora básica, en la cual le piden a la persona que ingrese dos valores numéricos y le pregunta también el tipo de operación que quiere aplicar como suma, resta, multiplicación o división. En la consola se imprime la operación y el resultado de este.

`get_user_input():` Esta función solicita al usuario dos números y la operación que desea realizar. Si se introduce una entrada no numérica, atrapa la excepción ValueError y vuelve a pedir la entrada.

`ejecutar_operacion(user_input, operations):` Esta función toma la entrada del usuario (números y operación) y un diccionario de operaciones. Verifica si la operación ingresada está en el diccionario y ejecuta la operación correspondiente utilizando funciones lambda almacenadas en el diccionario. Muestra el resultado de la operación.

`main():` La función principal del programa. Define un diccionario llamado operations que mapea los símbolos de operación a funciones lambda correspondientes (suma, resta, multiplicación, división). En un bucle infinito, obtiene la entrada del usuario, verifica si la operación es válida y la ejecuta llamando a la `función ejecutar_operacion()`. El bucle continúa hasta que el usuario escribe 'exit' para salir del programa.

La ejecución principal del programa se encuentra en if __name__ == "__main__":, lo que significa que el código dentro de este bloque se ejecutará si este archivo es el archivo principal que se está ejecutando.

`<stdio.h>`



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
