def get_user_input():
    try:
        # Solicita al usuario dos números y la operación a realizar
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(user_input, operations):
    num1, num2, operation = user_input
    # Verifica si la operación ingresada está en el diccionario de operaciones
    if operation in operations:
        # Ejecuta la operación correspondiente utilizando la función lambda almacenada en el diccionario
        result = operations[operation](num1, num2)
        print("Resultado:", result)
    else:
        print("Operacion invalida")

def main():
    # Diccionario que mapea los símbolos de operación a funciones lambda correspondientes
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Division por cero"
    }

    while True:
        # Obtiene la entrada del usuario
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        # Verifica si la operación ingresada está en el diccionario de operaciones
        if user_input[2] in operations:
            # Ejecuta la operación utilizando la función ejecutar_operacion
            ejecutar_operacion(user_input, operations)
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o escriba 'exit' para salir.")

if __name__ == "__main__":
    main()
