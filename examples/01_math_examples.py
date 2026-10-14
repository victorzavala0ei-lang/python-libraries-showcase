"""
Ejemplos de la librería estándar 'math' en Python.

La librería 'math' proporciona acceso a funciones matemáticas definidas
por el estándar de C para números de punto flotante y enteros.
"""

import math

def demostracion_constantes():
    print("=" * 60)
    print("1. CONSTANTES MATEMÁTICAS")
    print("=" * 60)
    print(f"Pi (π):                {math.pi:.10f}")
    print(f"Número de Euler (e):   {math.e:.10f}")
    print(f"Tau (2π):              {math.tau:.10f}")
    print(f"Infinito positivo:     {math.inf}")
    print(f"NaN (Not a Number):    {math.nan}")
    print()

def demostracion_redondeo_y_valor_absoluto():
    print("=" * 60)
    print("2. REDONDEO Y VALOR ABSOLUTO")
    print("=" * 60)
    numero = 7.65
    negativo = -14.28
    
    print(f"Número original:       {numero}")
    print(f"Techo (ceil):          {math.ceil(numero)}  (entero más cercano >= x)")
    print(f"Piso (floor):          {math.floor(numero)} (entero más cercano <= x)")
    print(f"Truncado (trunc):      {math.trunc(numero)} (elimina la parte decimal)")
    print(f"Valor absoluto (fabs): {math.fabs(negativo)} de {negativo}")
    print()

def demostracion_potencias_y_raices():
    print("=" * 60)
    print("3. POTENCIAS Y RAÍCES")
    print("=" * 60)
    base = 5
    exponente = 3
    numero_raiz = 144
    
    print(f"Potencia ({base}^{exponente}):        {math.pow(base, exponente)}")
    print(f"Raíz cuadrada de {numero_raiz}:   {math.sqrt(numero_raiz)}")
    print(f"Raíz entera de 50:         {math.isqrt(50)} (el entero más grande cuyo cuadrado <= 50)")
    print()

def demostracion_trigonometria():
    print("=" * 60)
    print("4. TRIGONOMETRÍA Y CONVERSIÓN DE ÁNGULOS")
    print("=" * 60)
    grados = 45.0
    radianes = math.radians(grados)
    
    print(f"Ángulo en grados:          {grados}°")
    print(f"Convertido a radianes:     {radianes:.6f} rad (math.radians)")
    print(f"Seno de {grados}°:             {math.sin(radianes):.6f}")
    print(f"Coseno de {grados}°:           {math.cos(radianes):.6f}")
    print(f"Tangente de {grados}°:         {math.tan(radianes):.6f}")
    
    hipotenusa = math.hypot(3, 4)
    print(f"Hipotenusa de catetos 3 y 4: {hipotenusa}")
    print()

def demostracion_logaritmos_y_exponenciales():
    print("=" * 60)
    print("5. LOGARITMOS Y EXPONENCIALES")
    print("=" * 60)
    x = 100
    print(f"Logaritmo natural (ln) de {x}:  {math.log(x):.6f}")
    print(f"Logaritmo base 10 de {x}:       {math.log10(x):.6f}")
    print(f"Logaritmo base 2 de 64:         {math.log2(64):.6f}")
    print(f"Logaritmo de 81 en base 3:      {math.log(81, 3):.6f}")
    print(f"Exponencial e^2:                {math.exp(2):.6f}")
    print()

def demostracion_teoria_numeros():
    print("=" * 60)
    print("6. COMBINATORIA Y TEORÍA DE NÚMEROS")
    print("=" * 60)
    a, b = 48, 18
    print(f"M.C.D. (gcd) de {a} y {b}:       {math.gcd(a, b)}")
    print(f"M.C.M. (lcm) de {a} y {b}:       {math.lcm(a, b)}")
    print(f"Factorial de 6 (6!):             {math.factorial(6)}")
    print(f"Combinaciones (10 en 3):         {math.comb(10, 3)}")
    print(f"Permutaciones (10 en 3):         {math.perm(10, 3)}")
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'math' EN PYTHON <<<\n")
    demostracion_constantes()
    demostracion_redondeo_y_valor_absoluto()
    demostracion_potencias_y_raices()
    demostracion_trigonometria()
    demostracion_logaritmos_y_exponenciales()
    demostracion_teoria_numeros()
    print("¡Demostración de 'math' completada con éxito!\n")

if __name__ == "__main__":
    main()
