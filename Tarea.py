def decorador(funcion):
    def wrapper():
        print("[DEBUG] Iniciando ejecución de la función...")
        a = funcion()
        print("Escribiendo despues de la funcion")
        return a
    return wrapper

@decorador
def escribir():
    print("Escrito por la funcion")

escribir()
