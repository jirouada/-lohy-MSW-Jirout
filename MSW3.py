import numpy as np
import matplotlib.pyplot as plt
import time
import random

def jacobi(A, b, niteraci):
    x0=np.ones(len(A))
    x = x0
    D = np.diag(A)
    L = np.tril(A, k = -1)
    U = np.triu(A, k = 1)
    for i in range(niteraci):
        x = (b - np.matmul((L + U),x))/D
    return x

def gauss_seidel(A, b, niteraci):
    x0=np.ones(len(A))
    x = x0
    U = np.triu(A, k = 1)
    Lstar = np.tril(A, k = 0)               
    T = np.matmul(-np.linalg.inv(Lstar), U) 
    C = np.matmul(np.linalg.inv(Lstar), b)  
    for i in range(niteraci):
        x = np.matmul(T, x) + C            
    return x

primycas = []
primycas2 = []
intcas =[] 
intcas2 =[] 

for i in range (10,201,10):
    a = np.random.randint(1, 100, size=(i, i))
    b = [random.randint(1, 100) for _ in range(i)]
    pocet_mereni = 10
    sumcasp=0
    sumcasp2= 0
    sumcasi = 0
    sumcasi2 = 0
    
    for _ in range(pocet_mereni):
        start = time.time()
        np.linalg.solve(a,b)
        end = time.time()
        sumcasp += (end-start)

    for _ in range(pocet_mereni):
        start = time.time()
        jacobi(a,b,3)
        end = time.time()
        sumcasi += (end-start)
        
    for _ in range(pocet_mereni):
        start = time.time()
        gauss_seidel(a,b,3)
        end = time.time()
        sumcasi2 += (end-start)

    for _ in range(pocet_mereni):
        start = time.time()
        np.linalg.inv(a).dot(b)
        end = time.time()
        sumcasp2 += (end-start)   
        
    
    primycas.append(sumcasp/pocet_mereni)
    primycas2.append(sumcasp2/pocet_mereni)
    intcas.append(sumcasi/pocet_mereni)
    intcas2.append(sumcasi2/pocet_mereni)

znaceni = [f"{i}x{i}" for i in range(10,201,10)]

plt.plot(znaceni,primycas, marker='o', linestyle='-')
plt.plot(znaceni,intcas, marker='o', linestyle='-')
plt.plot(znaceni,intcas2, marker='o', linestyle='-')
plt.plot(znaceni,primycas2, marker='o', linestyle='-')
plt.xticks(rotation = 90)
plt.legend(labels = ["Přímý", "Jacobi", "Gauss Seidel", "Přímý s inverzní maticí"],loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel("Čas pro výpočet (v sekundách)")
plt.show()

