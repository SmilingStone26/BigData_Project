import csv
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import cluster

csvFile = open("Resource/winequality-white.csv", encoding='utf-8')
readFile = list(csv.reader(csvFile, delimiter = ";"))

fixed_acidity = []
volatile_acidity = []
citric_acid = []
residual_sugar = []
chloride = []
free_sulfure_dioxyde = []
total_sulfur_dioxyde = []
density = []
pH = []
sulphates = []
alcohol = []
quality = []

for i in range(1,len(readFile)):
    fixed_acidity.append(readFile[i][0])
    volatile_acidity.append(readFile[i][1])
    citric_acid.append(readFile[i][2])
    residual_sugar.append(readFile[i][3])
    chloride.append(readFile[i][4])
    free_sulfure_dioxyde.append(readFile[i][5])
    total_sulfur_dioxyde.append(readFile[i][6])
    density.append(readFile[i][7])
    pH.append(readFile[i][8])
    sulphates.append(readFile[i][9])
    alcohol.append(readFile[i][10])
    quality.append(readFile[i][11])
"""
plt.scatter(fixed_acidity, quality,  marker='o')
plt.show()
plt.scatter(volatile_acidity,quality, marker='o')
plt.show()
plt.scatter(citric_acid, quality, marker='o')
plt.show()
plt.scatter(residual_sugar, quality, marker='o')
plt.show()
plt.scatter(chloride, quality, marker='o')
plt.show()
plt.scatter(free_sulfure_dioxyde, quality, marker='o')
plt.show()
plt.scatter(total_sulfur_dioxyde, quality, marker='o')
plt.show()
plt.scatter(density, quality, marker='o')
plt.show()
plt.scatter(pH, quality, marker='o')
plt.show()
plt.scatter(sulphates, quality, marker='o')
plt.show()
plt.scatter(alcohol, quality, marker='o')
plt.show()
"""

file = pd.read_csv('Resource/winequality-white.csv')
data = file.stack()
mat = data.values

km = cluster.KMeans(n_clusters=6)
km.fit(mat)
label = km.labels_
result = pd.DataFrame([file.index, label]).T
