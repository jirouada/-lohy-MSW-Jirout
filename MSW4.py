import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize as sop
import time


def pf(x):
    return (x**2) + 2*x - 11

def ef(x):
    return 3**x - 11

def hf(x):
    return 4*np.sin(x)-2

def dpf(x):
    return 2*x + 2

def d_ef(x):
    return (3**x)*np.log(3) 
 
def dhf(x):
    return 4*np.cos(x)

bisekce_casy = []
newton_casy = []
bisekce_vysledky = []
newton_vysledky = []

start = time.time()
k1_p_b = sop.bisect(pf, 2, 3)
k2_p_b = sop.bisect(pf, -5, -4)
stop = time.time()
bisekce_vysledky.append(k1_p_b)
bisekce_vysledky.append(k2_p_b)
bisekce_casy.append(stop-start)

start = time.time()
k1_p_n = sop.newton(pf, 2.5, dpf, maxiter=5)
k2_p_n = sop.newton(pf, -4.5, dpf, maxiter=5)
stop = time.time()
newton_vysledky.append(k1_p_n)
newton_vysledky.append(k2_p_n)
newton_casy.append(stop-start)

start = time.time()
k_e_b = sop.bisect(ef, 2, 3) #Změna znaménka je sdílena v bodech
stop = time.time()
bisekce_vysledky.append(k_e_b)
bisekce_casy.append(stop-start)

start = time.time()
k_e_n = sop.newton(ef, 2.5, d_ef, maxiter=5) #Změna znaménka je sdílena v bodech
stop = time.time()
newton_vysledky.append(k_e_n)
newton_casy.append(stop-start)

start = time.time()
k_h_b = sop.bisect(hf, 0, 1) 
stop = time.time()
bisekce_vysledky.append(k_h_b)
bisekce_casy.append(stop-start)

start = time.time()
k_h_n = sop.newton(hf, 0.5, dhf, maxiter=5) 
stop = time.time()
newton_vysledky.append(k_h_n)
newton_casy.append(stop-start)

print(bisekce_casy)
print(newton_casy)
print(bisekce_vysledky)
print(newton_vysledky)

znacky = ["Polynom", "Exponencial", "Harmonic"]


i = np.arange(3)
width = 0.4
plt.bar(i-0.2, bisekce_casy, width, label="Bisekce")
plt.bar(i+0.2, newton_casy, width, label = "Newton")
plt.xticks(i,znacky)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel("Čas pro výpočet (v sekundách)")
plt.show()

