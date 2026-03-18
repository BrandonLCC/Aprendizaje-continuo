# Funciones anidadas
def funcion_principal():
    def funcion_anidada():
        print("Esta es una función anidada")
    funcion_anidada()

# Funciones lambda
suma = lambda x, y: x + y

# Funciones recursivas
def factorial(n):
    if n == 0:
        return 1    

    else:
        return n * factorial(n - 1)

# Funciones con argumentos por defecto
def saludar(nombre="Mundo"):
    print(f"Hola, {nombre}!")
# Funciones con argumentos variables
def sumar(*numeros):
    return sum(numeros)

# Funciones con argumentos de palabra clave
def imprimir_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

# funciones mas avanzadas
def decorador(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Antes de la función")
        resultado = funcion(*args, **kwargs)
        print("Después de la función")
        return resultado
    return funcion_decorada
@decorador
def funcion_a_decorar():
    print("Esta es la función a decorar")

# Funciones generadoras
def generador():
    for i in range(5):
        yield i

# Funciones de orden superior
def aplicar_funcion(funcion, valor):
    return funcion(valor)

# Funciones anónimas
def aplicar_funcion_anónima(valor):
    return (lambda x: x * 2)(valor)

# Funciones con anotaciones de tipo
def sumar_con_tipos(a: int, b: int) -> int:
    return a + b

# Funciones con manejo de excepciones
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    
# Funciones con documentación
def funcion_con_documentacion():
    """
    Esta función no hace nada pero tiene documentación.
    """
    pass

# Funciones con variables globales
contador = 0
def incrementar_contador():
    global contador
    contador += 1
    return contador

# Funciones con variables locales
def funcion_con_variable_local():
    variable_local = "Esta es una variable local"
    print(variable_local)

# Funciones con retorno de múltiples valores
def retornar_multiples_valores():
    return "Valor 1", "Valor 2", "Valor 3"

# Funciones con argumentos de tipo variable
def funcion_con_argumentos_variables(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos de palabra clave:", kwargs)

# Funciones con argumentos de tipo variable y retorno de múltiples valores
def funcion_compleja(*args, **kwargs):
    resultado = sum(args) + sum(kwargs.values())
    return resultado, "Resultado calculado"

# Funciones con anotaciones de tipo y manejo de excepciones
def dividir_con_tipos(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    
# Funciones con documentación y manejo de excepciones
def funcion_con_documentacion_y_excepciones():
    """
    Esta función intenta dividir dos números y maneja la excepción de división por cero.
    """
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = a / b
        print(f"El resultado de {a} dividido por {b} es: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except ValueError:
        print("Por favor, ingrese un número válido")

# Funciones con variables globales y manejo de excepciones
contador_global = 0
def incrementar_contador_global():

    global contador_global
    try:
        contador_global += 1
        return contador_global
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# funcion de lista de funciones
def lista_de_funciones():
    def funcion1():
        print("Función 1")
    def funcion2():
        print("Función 2")
    def funcion3():
        print("Función 3")
    return [funcion1, funcion2, funcion3]


# Funciones con argumentos de tipo variable, retorno de múltiples valores, anotaciones de tipo y manejo de excepciones
#def funcion_compleja_con_tipos(*args: int, **kwargs: int) ->
#    int:
#    """
#    Esta función suma todos los argumentos posicionales y de palabra clave, y maneja cualquier excepción que pueda ocurrir.
#    """
#    try:
#        resultado = sum(args) + sum(kwargs.values())
#        return resultado
#    except Exception as e:
#        print(f"Ocurrió un error: {e}")
#        return 0    
    

# que funciones son escenaciles para aprender?