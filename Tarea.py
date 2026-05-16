def decorador(funcion):
    def wrapper():
        print("Escribiendo antes de la funcion")
        a = funcion()
        print("Escribiendo despues de la funcion")
        return a
    return wrapper

@decorador
def escribir():
    print("Escrito por la funcion")

escribir()
