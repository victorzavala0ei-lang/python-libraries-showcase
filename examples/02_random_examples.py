"""
Ejemplos de la librería estándar 'random' en Python.

La librería 'random' implementa generadores de números pseudoaleatorios
para varias distribuciones numéricas y operaciones sobre secuencias.
"""

import random

def demostracion_enteros_aleatorios():
    print("=" * 60)
    print("1. GENERACIÓN DE ENTEROS")
    print("=" * 60)
    # randint(a, b) incluye tanto 'a' como 'b'
    dado = random.randint(1, 6)
    print(f"Lanzamiento de dado (1-6):         {dado}")
    
    # randrange(start, stop, step) similar a range()
    par_aleatorio = random.randrange(10, 30, 2)
    print(f"Número par aleatorio [10, 30):     {par_aleatorio}")
    print()

def demostracion_flotantes_aleatorios():
    print("=" * 60)
    print("2. GENERACIÓN DE FLOTANTES Y DISTRIBUCIONES")
    print("=" * 60)
    # random() devuelve un flotante uniforme en el intervalo [0.0, 1.0)
    flotante_0_1 = random.random()
    print(f"Flotante aleatorio en [0.0, 1.0):  {flotante_0_1:.6f}")
    
    # uniform(a, b) genera un flotante uniforme en [a, b]
    temperatura = random.uniform(15.5, 32.0)
    print(f"Temperatura simulada [15.5, 32.0]: {temperatura:.2f} °C")
    
    # gauss(mu, sigma) distribución normal o gaussiana
    media, desviacion = 100, 15
    coeficiente = random.gauss(media, desviacion)
    print(f"Valor con distribución normal (μ={media}, σ={desviacion}): {coeficiente:.2f}")
    print()

def demostracion_secuencias():
    print("=" * 60)
    print("3. OPERACIONES CON SECUENCIAS (LISTAS)")
    print("=" * 60)
    lenguajes = ["Python", "JavaScript", "Rust", "Go", "C++", "Java"]
    print(f"Lista original: {lenguajes}")
    
    # choice(seq): elige un único elemento aleatorio
    elegido = random.choice(lenguajes)
    print(f"Elemento único elegido (choice):   {elegido}")
    
    # sample(seq, k): k elementos aleatorios sin repetición
    muestra = random.sample(lenguajes, k=3)
    print(f"Muestra de 3 sin reemplazo:        {muestra}")
    
    # choices(seq, weights=..., k=...): selección con reemplazo y probabilidades
    colores = ["Rojo", "Verde", "Azul"]
    ponderacion = [0.7, 0.2, 0.1]  # 70% Rojo, 20% Verde, 10% Azul
    sorteo = random.choices(colores, weights=ponderacion, k=5)
    print(f"5 selecciones ponderadas:          {sorteo}")
    
    # shuffle(x): mezcla los elementos de una lista in-place
    baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(baraja)
    print(f"Lista barajada in-place:           {baraja}")
    print()

def demostracion_semilla_reproducibilidad():
    print("=" * 60)
    print("4. REPRODUCIBILIDAD MEDIANTE SEMILLAS (SEED)")
    print("=" * 60)
    print("Al establecer una semilla fija, los resultados son deterministas:")
    random.seed(42)
    primera_serie = [random.randint(1, 100) for _ in range(5)]
    print(f"Serie con semilla 42:              {primera_serie}")
    
    # Si reiniciamos la misma semilla:
    random.seed(42)
    segunda_serie = [random.randint(1, 100) for _ in range(5)]
    print(f"Misma serie repitiendo semilla:    {segunda_serie}")
    print(f"¿Son exactamente idénticas?:       {primera_serie == segunda_serie}")
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'random' EN PYTHON <<<\n")
    demostracion_enteros_aleatorios()
    demostracion_flotantes_aleatorios()
    demostracion_secuencias()
    demostracion_semilla_reproducibilidad()
    print("¡Demostración de 'random' completada con éxito!\n")

if __name__ == "__main__":
    main()
