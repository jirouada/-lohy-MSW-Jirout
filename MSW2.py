import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Import dat
data = pd.read_csv('/Users/adamjirout/Downloads/car_data.csv')

#Analýza převodovek
label_transmission = "Auto","Manual"
Transmissions=[int(data['Transmission'].value_counts()['Auto']),int(data['Transmission'].value_counts()['Manual'])]

plt.pie(Transmissions, labels = label_transmission, autopct='%1.1f%%')
plt.show()
    
znacky = data.Company.unique()
znacky.sort()
autocount = [] 
for i in znacky:
    autocount.append(data['Transmission'].value_counts()['Auto'] and data['Company'].value_counts()[i])

plt.bar(znacky,autocount)
plt.xticks(rotation=90)
plt.show()

#Analýza průměrného příjmu a cen
prumerprijemz=(data[['Company','Annual Income']].groupby('Company').mean())
prumercena=(data[['Company','Price ($)']].groupby('Company').mean())

plt.subplot(2,1,1)
plt.bar(znacky, prumerprijemz['Annual Income'])
plt.xticks([])
plt.ylabel('Pruměrný příjem na značku')

plt.subplot(2,1,2)
plt.bar(znacky, prumercena['Price ($)'], color = 'green')
plt.ylabel('Průměrná cena na značku')
plt.xticks(znacky, rotation=90)
plt.show()

#Trend nákupů
data['Date'] = pd.to_datetime(data['Date'])

data['Month'] = data['Date'].dt.month #meziproces na třídění
data['Year'] = data['Date'].dt.year

mesicni_prumer = data.groupby(['Year', 'Month'])['Price ($)'].sum()

mesicni_prumer = mesicni_prumer.reset_index()
fmesicniprumer = mesicni_prumer.pivot(index='Month', columns='Year', values='Price ($)')
print(fmesicniprumer)

plt.plot(fmesicniprumer.index, fmesicniprumer[2022], marker='o', linestyle='-', label = '2023')
plt.plot(fmesicniprumer.index, fmesicniprumer[2023], marker='o', linestyle='-', label ='2024')
plt.title('Tržby nakoupených aut za jednotlivé měsíce')
plt.xlabel('Měsíc')
plt.ylabel('Tržby (v desetimil. $)')
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()

#Typy vozidel
typesofcar = data.groupby(['Company', 'Body Style'])['Body Style'].value_counts()
typesofcar = typesofcar.reset_index()
typesofcar = typesofcar.pivot(index='Company', columns='Body Style', values='count')
typesofcar.fillna(0, inplace=True)
types_percentage = typesofcar.div(typesofcar.sum(axis=1), axis=0) * 100
print(types_percentage)

print(typesofcar)
n = len(znacky)
ind = np.arange(n)   
width = 0.50
bottom = [0] * n   

for car_type in ['Hardtop', 'Hatchback', 'Passenger', 'SUV', 'Sedan']:
    plt.bar(ind, types_percentage[car_type], width, bottom=bottom, label=car_type)
    bottom = [bottom[i] + types_percentage[car_type][i] for i in range(len(znacky))]

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel('Zastoupení typu aut (v %)')
plt.xticks(ind, znacky, rotation=90)
plt.show()

typespie = []
for i in ['Hardtop', 'Hatchback', 'Passenger', 'SUV', 'Sedan']:
    typespie.append(data['Body Style'].value_counts()[i])

print(typespie)
label = ['Hardtop', 'Hatchback', 'Passenger', 'SUV', 'Sedan']
plt.pie(typespie, labels = label, autopct='%1.1f%%')
plt.show()

#První verze skládaného grafu, hází špatné hodnoty a obsahuje 2x SUV
#plt.bar(ind, typesofcar['Hardtop'], width, color = 'blue', label = 'Hardtop')
#plt.bar(ind, typesofcar['Hatchback'], width, bottom= typesofcar['Hardtop'],color = 'green', label = 'Hatchback')
#plt.bar(ind, typesofcar['Passenger'], width, bottom= typesofcar['Hatchback'],color = 'red', label = 'Passenger')
#plt.bar(ind, typesofcar['SUV'], width, bottom= typesofcar['Passenger'],color = 'cyan', label = 'Suv')
#plt.bar(ind, typesofcar['Sedan'], width, bottom= typesofcar['SUV'],color = 'purple', label = 'Sedan')