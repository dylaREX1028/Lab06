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

#### Demostración del código y paquetes de python3
https://docs.google.com/document/d/17TSKtezFcUdfuH16HlHy4H3ENoS90FVvZUkp7k9rEgQ/edit?usp=sharing

`sudo apt update`
`sudo apt install python3`


## Calculadora
La finalidad de laboratorio es una calculadora básica, en la cual le piden a la persona que ingrese dos valores numéricos y le pregunta también el tipo de operación que quiere aplicar como suma, resta, multiplicación o división. En la consola se imprime la operación y el resultado de este.

`get_user_input():` Esta función se le solicita al usuario dos números y la operación que desea realizar. Si este digita un valor no numérica, reca en ValueError y vuelve a pedir la entrada.

`ejecutar_operacion(user_input, operations):` En esta función se toma la entrada el números y operación mediante un diccionario de operaciones. Se verifica si la operación ingresada está en el diccionario y aplica la operación utilizando funciones lambda almacenadas en el diccionario. 

`main():` Esta es la función principal del programa. Se define un diccionario llamado operations que mapea los símbolos de operación a funciones lambda. Mediante un bucle infinito, obtiene la entrada del usuario, verifica si la operación es válida y la ejecuta llamando a la `función ejecutar_operacion()`. El bucle continúa hasta que el usuario escribe 'exit' para salir del programa. Este se aplica cuando le piden ingresar el tipo de operación

Finalmente, laa ejecución principal del programa se encuentra en `if __name__ == "__main__":`, lo que significa que el código dentro de este bloque se ejecutará si este archivo es el archivo principal que se está ejecutando.

  
Este se corre con lo siguiente: `python3 calculadora_modi.py`


## Callbacks
La finalidad de código datamanager.py. radica en  la simulación de datos en tiempo real cuando hay actualizaciones en los datos de temperatura y humedad. Se estará usando también el código de que la profesora nos brindó de eventos.py el cual gestiona la suscripción a eventos y notifica a los suscriptores cuando se produce un evento específico. En este caso se va describir el código modificado de datamanager.py.

`Clase RealTimeDataManager:` Esta clase inicializa un diccionario de datos que representa la temperatura y la humedad. También crea una instancia de `EventManager` para gestionar la publicación y suscripción a eventos.

`Método start_real_time_updates():` Se ejecuta un bucle infinito que simula actualizaciones de datos en tiempo real. Cada 3 segundos, llama al método `generate_real_time_data()` para actualizar los valores de temperatura y humedad y luego notifica al `EventManager` que los datos han cambiado.

`Método generate_real_time_data():` Se genera datos aleatorios para simular cambios en la temperatura y la humedad.

Creación de instancias y ejecución en segundo plano: Se crea una instancia de `RealTimeDataManager` y se inicia un hilo `(thread)` para ejecutar `start_real_time_updates()` en segundo plano. Esto simula la actualización continua de datos.

`Callback print_updated_data(data):` Se define una función de callback que imprime los datos actualizados al `stdout` (la consola). Este callback se suscribe al `EventManager` para el evento `"datos_actualizados"`.

Bucle `try-except` para mantener el programa en funcionamiento: El programa se mantiene en un bucle infinito (excepto cuando se interrumpe con Ctrl + C) para permitir que los hilos se ejecuten y manejar la interrupción del teclado de manera adecuada.












