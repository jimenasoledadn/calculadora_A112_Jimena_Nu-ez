def limpiar_pantalla():
    import os
    os.system("cls")

def pausar():
    import os
    os.system("pause")

def menu_calculadora()->str:
    """Muestra el menu de opciones de la calculadora

    Returns:
        str: devuelve la opcion seleccionada
    """
    limpiar_pantalla()
    print(f"{'Calculadora':^25s}")
    print(f"{'-----------':^25s}") 
    print(" Opciones: ")
    print("1- Ingresar 1er operando A: ")
    print("2- Ingresar 2do operando B: ")
    print("3- Calcular todas las operaciones ")
    print("4- Informar resultados")
    print("5- Salir")

    return input("Ingrese opcion: ")

def pedir_operando_primero()->int:
    """Pide un numero por consola y lo convierte en entero, para luego retornarlo

    Raises:
        ValueError: valida que sea un entero natural

    Returns:
        int: retorna un entero
    """
    operando = int(input("A: "))
    if isinstance(operando, int):
        return operando
    raise ValueError("Debe ingresar un numero")

def pedir_operando_segundo()->int:
    """Pide un numero por consola y lo convierte en entero, para luego retornarlo

    Raises:
        ValueError: valida que sea un entero natural

    Returns:
        int: retorna un entero
    """
    operando = int(input("B: "))
    if isinstance(operando, int):
        return operando
    raise ValueError("Debe ingresar un numero")

def pedir_confirmacion(mensaje:str)->bool: 
    """Muestra un mensaje por pantalla para pedir confirmacion de salida del programa

    Args:
        mensaje (str): pregunta al usuario si quiere seguir en el programa o salir

    Returns:
        bool: indica la letra de salida
    """
    rta = input(mensaje).lower()
    return rta == "s"

def sumar(a:int, b:int)->int :
    # Documentacion
    """suma de dos numeros enteros 

    Args:
        a (int): primer numero a sumar
        b (int): segundo numero a sumar

    Returns:
        int: resulado de sumar a y b 
    """
    if not isinstance(a, int):
        raise ValueError("El primer operando debe ser un numero")
    if not isinstance(b, int):
        raise ValueError("El segundo operando debe ser un numero")
    
    return a + b   

def restar(a:int, b:int)->int :
    # Documentacion
    """Resta de dos numeros enteros 

    Args:
        a (int): primer numero a restar
        b (int): segundo numero a restar

    Returns:
        int: resulado de la resta entre a y b 
    """
    if not isinstance(a, int):
        raise ValueError("El primer operando debe ser un numero")
    if not isinstance(b, int):
        raise ValueError("El segundo operando debe ser un numero")

    return a - b

def dividir(a:int, b:int)->float:
    """ Division de dos numeros enteros

    Args:
        a (int): recien un numero entero, el dividendo
        b (int): recibe un segundo numero entero, el divisor

    Returns:
        float: Devuelve el resultado de la division, cociente
    """
    if b < 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    else:
        return a / b

def multiplicar(a:int, b:int)->int:
    """Multiplica los dos numeros que le llegan por parametro

    Args:
        a (int): multiplicando     
        b (int): multiplicador  

    Returns:
        int: el producto del multiplicador con el multiplicando
    """
    if not isinstance(a, int):
        raise ValueError("El primer operando debe ser un numero")
    if not isinstance(b, int):
        raise ValueError("El segundo operando debe ser un numero")

    return a * b 

def factorial(n:int)->int:
    """Clacula el factorial de un numero

    Args:
        n (int): numero a calcular

    Raises:
        ValueError: valida entero natural
        TypeError: valida tipo entero

    Returns:
        int: Factorial del numero ingresado
    """
    if isinstance(n, bool):
        raise TypeError("No aceptamos booleanos")
    elif isinstance(n , int): 
        if n < 0: 
            raise ValueError("No esta definido el factorial de un negativo")
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    else:
        raise TypeError("Eso no es un numero") 