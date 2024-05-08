import numpy as np
import scipy as sp

#Připravené funkce pro pokročilejší řešení.
def pf(x):
    return x**2 + 2*x - 11

def ef(x):
    return 3**x - 11

def hf(x):
    return 4*np.sin(x) - 2

#Analytická řešení ručně připravená pro definované funkce. Lze měnit krajní body.
def a_pf(a,b):
    return ((1/3*(b**3) + b**2 - 11*b) - (1/3 * a**3 + a**2 - 11*a))

def a_ef(a,b):
    return ((1/np.log(3)) * (3**b - 3**a) - 11 * (b - a))
    
def a_hf(a,b):
    return 4*((-np.cos(b)) - (-np.cos(a))) + ((-2*b)-(-2*a))

#Riemann - leve obdelníky
def riemann(f, a, b, n):
    h = (b - a) / n
    sum_left = sum(f(a + i*h) for i in range(n))
    return sum_left * h


a = 0
b = np.pi
n = 1000 #množství intervalů mezi body

#příprava pro simpson
x = np.linspace(a,b,n)
y1= pf(x)
y2= ef(x)
y3 = hf(x)

# Výpočet integrálu pomocí riemana
r_pf = riemann(pf, a,b, n)
r_ef = riemann(ef, a,b, n)
r_hf = riemann(hf, a,b, n)

# Výpis výsledků
print("Analytické řešení - polynom:", a_pf(a,b))
print("Riemann řešení - polynom", r_pf)
print("Simpson řešení - polynom", sp.integrate.simps(y1,x))
print("-"*100)
print("Analytické řešení - exponencial:", a_ef(a,b))
print("Riemann řešení - exponencial", r_ef)
print("Simpson řešení - exponencial", sp.integrate.simps(y2,x))
print("-"*100)
print("Analytické řešení - harmonicka:", a_hf(a,b))
print("Riemann řešení - harmonicka", r_hf)
print("Simpson řešení - harmonicka", sp.integrate.simps(y3,x))