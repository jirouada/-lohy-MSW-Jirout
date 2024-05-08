import numpy as np

def f(x):
    return ((x**2) + 2*x + 1)

def f2(x):
    return np.sin(100 * x)

def adapt_derivace(funkce, x, k=1e-6, tolerance=1e-7):
    predchozi = (funkce(x + k) - funkce(x - k)) / (2 * k)
    aktualni = predchozi + tolerance * 2 
    while abs(aktualni - predchozi) > tolerance:
        predchozi = aktualni
        k /= 2
        aktualni = (funkce(x + k) - funkce(x - k)) / (2 * k)
    return aktualni

def static_derivace(funkce, x, k=1e-6):
    return (funkce(x + k) - funkce(x - k)) / (2 * k)

def analytic_derivace(x): #Ručně spočítaná derivace funkce f(x)
    return (2*x + 2)

def analytic_derivace2(x): #Ručně spočítaná derivace funkce f2(x)
    return 100 * np.cos(100 * x)

x = 2.0  
adapt = adapt_derivace(f, x)
static = static_derivace(f, x)
analytic = analytic_derivace(x)

x1=1
adapt2 = adapt_derivace(f2, x1)
static2 = static_derivace(f2, x1)
analytic2 = analytic_derivace2(x1)


print("Derivace s adaptivním krokem:", adapt2)
print("Statická derivace:", static2)
print("Analytic derivace:", analytic2)

print((analytic2-adapt2))
print(analytic2-static2)
print((analytic2-adapt2)-(analytic2-static2))

print(100*"-")

print("Derivace s adaptivním krokem:", adapt)
print("Statická derivace:", static)
print("Analytic derivace:", analytic)

print((analytic-adapt))
print(analytic-static)
print((analytic-adapt)-(analytic-static))