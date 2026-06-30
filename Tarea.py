def decorador(funcion):
    def wrapper():
        print(">>> Preparando el entorno antes de llamar a la función.")
        a = funcion()
        print("Escribiendo despues de la funcion")
        return a
    return wrapper

@decorador
def escribir():
    print("Escrito por la funcion")

escribir()
