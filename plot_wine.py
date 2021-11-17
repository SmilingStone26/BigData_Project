import csv
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import cluster

axe_X = 7
axe_Y = 10
liste_type = ["Type", "Fixed acidity", "Volatile acidity", "Citric acid", "Residual sugar", "Chlorides", "Free sulfur dioxyde", "Total sulfur dioxide", "Density", "pH", "Sulphates", "Alcohol", "Quality"]
csvFile = open("Resource/winequality-white.csv", encoding='utf-8')
readFile = list(csv.reader(csvFile, delimiter = ";"))

white_wine = []

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
    fixed_acidity.append(float(readFile[i][0]))
    volatile_acidity.append(float(readFile[i][1]))
    citric_acid.append(float(readFile[i][2]))
    residual_sugar.append(float(readFile[i][3]))
    chloride.append(float(readFile[i][4]))
    free_sulfure_dioxyde.append(float(readFile[i][5]))
    total_sulfur_dioxyde.append(float(readFile[i][6]))
    density.append(float(readFile[i][7]))
    pH.append(float(readFile[i][8]))
    sulphates.append(float(readFile[i][9]))
    alcohol.append(float(readFile[i][10]))
    quality.append(float(readFile[i][11]))
    white_wine.append([fixed_acidity[i-1],volatile_acidity[i-1],citric_acid[i-1],residual_sugar[i-1],chloride[i-1],free_sulfure_dioxyde[i-1],total_sulfur_dioxyde[i-1],density[i-1],pH[i-1],sulphates[i-1],alcohol[i-1],quality[i-1]])
csvFile.close()

csvFile = open("Resource/winequality-red.csv", encoding='utf-8')
readFile = list(csv.reader(csvFile, delimiter = ";"))

red_Wine = []

fixed_acidity.clear()
volatile_acidity.clear()
citric_acid.clear()
residual_sugar.clear()
chloride.clear()
free_sulfure_dioxyde.clear()
total_sulfur_dioxyde.clear()
density.clear()
pH.clear()
sulphates.clear()
alcohol.clear()
quality.clear()

for i in range(1,len(readFile)):
    fixed_acidity.append(float(readFile[i][0]))
    volatile_acidity.append(float(readFile[i][1]))
    citric_acid.append(float(readFile[i][2]))
    residual_sugar.append(float(readFile[i][3]))
    chloride.append(float(readFile[i][4]))
    free_sulfure_dioxyde.append(float(readFile[i][5]))
    total_sulfur_dioxyde.append(float(readFile[i][6]))
    density.append(float(readFile[i][7]))
    pH.append(float(readFile[i][8]))
    sulphates.append(float(readFile[i][9]))
    alcohol.append(float(readFile[i][10]))
    quality.append(float(readFile[i][11]))
    red_Wine.append([fixed_acidity[i-1],volatile_acidity[i-1],citric_acid[i-1],residual_sugar[i-1],chloride[i-1],free_sulfure_dioxyde[i-1],total_sulfur_dioxyde[i-1],density[i-1],pH[i-1],sulphates[i-1],alcohol[i-1],quality[i-1]])
csvFile.close()

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
"""
file = pd.read_csv('Resource/winequality-white.csv',)
data = file.stack()
mat = data.values

km = cluster.KMeans(n_clusters=6)
km.fit(mat)
label = km.labels_
result = pd.DataFrame([file.index, label]).T
"""

k_means_Red = cluster.KMeans(n_clusters=6,random_state=0)
k_means_Red.fit(red_Wine)
label_Red = k_means_Red.labels_
k_means_White = cluster.KMeans(n_clusters=6,random_state=0)
k_means_White.fit(white_wine)
label_White = k_means_White.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

White_Cluster_0 = []
White_Cluster_1 = []
White_Cluster_2 = []
White_Cluster_3 = []
White_Cluster_4 = []
White_Cluster_5 = []

for i in range(len(red_Wine)):
    if(label_Red[i] == 0):
        Red_Cluster_0.append(red_Wine[i])
    elif (label_Red[i] == 1):
        Red_Cluster_1.append(red_Wine[i])
    elif (label_Red[i] == 2):
        Red_Cluster_2.append(red_Wine[i])
    elif (label_Red[i] == 3):
        Red_Cluster_3.append(red_Wine[i])
    elif (label_Red[i] == 4):
        Red_Cluster_4.append(red_Wine[i])
    elif (label_Red[i] == 5):
        Red_Cluster_5.append(red_Wine[i])

for i in range(len(white_wine)):
    if(label_White[i] == 0):
        White_Cluster_0.append(white_wine[i])
    elif (label_White[i] == 1):
        White_Cluster_1.append(white_wine[i])
    elif (label_White[i] == 2):
        White_Cluster_2.append(white_wine[i])
    elif (label_White[i] == 3):
        White_Cluster_3.append(white_wine[i])
    elif (label_White[i] == 4):
        White_Cluster_4.append(white_wine[i])
    elif (label_White[i] == 5):
        White_Cluster_5.append(white_wine[i])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel(liste_type[axe_X])
ax.set_ylabel(liste_type[axe_Y])
plt.scatter([e[axe_X-1] for e in White_Cluster_0],[e[axe_Y-1] for e in White_Cluster_0], s=1, color = 'green')
plt.scatter([e[axe_X-1] for e in White_Cluster_1],[e[axe_Y-1] for e in White_Cluster_1], s=1, color = 'red')
plt.scatter([e[axe_X-1] for e in White_Cluster_2],[e[axe_Y-1] for e in White_Cluster_2], s=1, color = 'blue')
plt.scatter([e[axe_X-1] for e in White_Cluster_3],[e[axe_Y-1] for e in White_Cluster_3], s=1, color = 'yellow')
plt.scatter([e[axe_X-1] for e in White_Cluster_4],[e[axe_Y-1] for e in White_Cluster_4], s=1, color = 'black')
plt.scatter([e[axe_X-1] for e in White_Cluster_5],[e[axe_Y-1] for e in White_Cluster_5], s=1, color = 'purple')
plt.show()