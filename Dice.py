import random
import time

def lanzar_dados(amount, sides):
    """
    Lanza 'amount' dados, cada uno con 'sides' caras.
    Imprime el resultado de cada dado y al final imprime la lista total.
    """
    resultados = []  

    for i in range(amount):
        resultado = random.randint(1, sides)  # Número aleatorio entre 1 y sides
        resultados.append(resultado)          # Guardamos el resultado
        print(f"Lanzamiento {i+1}: {resultado}")  # Mostramos resultado en consola
        time.sleep(0.5)  # Pausa medio segundo para que se vea bien

    print(f"Resultado total: {resultados}")  # Al final mostramos todos los resultados

if __name__ == "__main__":
    # Aquí definimos cuántos dados lanzamos y de cuántas caras
    lanzar_dados(6, 6)
# Cambio de prueba para git
