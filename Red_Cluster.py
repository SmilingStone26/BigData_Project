import csv
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import cluster
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

axe_X = 7
axe_Y = 10
liste_type = ["Type", "Fixed acidity", "Volatile acidity", "Citric acid", "Residual sugar", "Chlorides", "Free sulfur dioxyde", "Total sulfur dioxide", "Density", "pH", "Sulphates", "Alcohol", "Quality"]
csvFile = open("Resource/winequality-red.csv", encoding='utf-8')
readFile = list(csv.reader(csvFile, delimiter = ";"))

red_Wine = []

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
    red_Wine.append([fixed_acidity[i-1],volatile_acidity[i-1],citric_acid[i-1],residual_sugar[i-1],chloride[i-1],free_sulfure_dioxyde[i-1],total_sulfur_dioxyde[i-1],density[i-1],pH[i-1],sulphates[i-1],alcohol[i-1],quality[i-1]])
csvFile.close()

#------------------------------------Clusterisation 1 --------------------------------------------------
"""
k_means_Red = cluster.KMeans(n_clusters=6,random_state=0)
k_means_Red.fit(red_Wine)
label_Red = k_means_Red.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

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

"""
"""fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel(liste_type[axe_X])
ax.set_ylabel(liste_type[axe_Y])
plt.scatter([e[axe_X-1] for e in Red_Cluster_0],[e[axe_Y-1] for e in Red_Cluster_0], s=1, color = 'green')
plt.scatter([e[axe_X-1] for e in Red_Cluster_1],[e[axe_Y-1] for e in Red_Cluster_1], s=1, color = 'red')
plt.scatter([e[axe_X-1] for e in Red_Cluster_2],[e[axe_Y-1] for e in Red_Cluster_2], s=1, color = 'blue')
plt.scatter([e[axe_X-1] for e in Red_Cluster_3],[e[axe_Y-1] for e in Red_Cluster_3], s=1, color = 'yellow')
plt.scatter([e[axe_X-1] for e in Red_Cluster_4],[e[axe_Y-1] for e in Red_Cluster_4], s=1, color = 'black')
plt.scatter([e[axe_X-1] for e in Red_Cluster_5],[e[axe_Y-1] for e in Red_Cluster_5], s=1, color = 'purple')
plt.show()"""
"""
plt.figure(1)
plt.subplot(211)
plt.scatter(quality,label_Red)
plt.subplot(212)
plt.hist2d(quality,label_Red, bins=6)
plt.show()
"""
#---------------------------------------- Clusterisation 2 ---------------------------------------------------
"""
red_Wine_2 = []

for i in range(len(red_Wine)):
    red_Wine_2.append([fixed_acidity[i], volatile_acidity[i], citric_acid[i], residual_sugar[i], chloride[i], free_sulfure_dioxyde[i], total_sulfur_dioxyde[i], density[i], pH[i], sulphates[i], alcohol[i]])

k_means_Red = cluster.KMeans(n_clusters=6,random_state=0)
k_means_Red.fit(red_Wine_2)
label_Red = k_means_Red.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

for i in range(len(red_Wine_2)):
    if(label_Red[i] == 0):
        Red_Cluster_0.append(red_Wine_2[i])
    elif (label_Red[i] == 1):
        Red_Cluster_1.append(red_Wine_2[i])
    elif (label_Red[i] == 2):
        Red_Cluster_2.append(red_Wine_2[i])
    elif (label_Red[i] == 3):
        Red_Cluster_3.append(red_Wine_2[i])
    elif (label_Red[i] == 4):
        Red_Cluster_4.append(red_Wine_2[i])
    elif (label_Red[i] == 5):
        Red_Cluster_5.append(red_Wine_2[i])

plt.figure(1)
plt.subplot(211)
plt.scatter(quality,label_Red)
plt.subplot(212)
plt.hist2d(quality,label_Red, bins=6)
plt.show()
"""
#---------------------------------------- Clusterisation 3 ---------------------------------------------------
red_Wine_3 = []

for i in range(len(red_Wine)):
    red_Wine_3.append([fixed_acidity[i] / 15.9, volatile_acidity[i]/1.58, citric_acid[i], residual_sugar[i]/15.5, chloride[i], free_sulfure_dioxyde[i]/72, total_sulfur_dioxyde[i]/289, density[i], pH[i]/4, sulphates[i]/2, alcohol[i]/14.9])

k_means_Red = cluster.KMeans(n_clusters=3,random_state=0)
k_means_Red.fit(red_Wine_3)
label_Red = k_means_Red.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

for i in range(len(red_Wine_3)):
    if(label_Red[i] == 0):
        Red_Cluster_0.append(red_Wine_3[i])
    elif (label_Red[i] == 1):
        Red_Cluster_1.append(red_Wine_3[i])
    elif (label_Red[i] == 2):
        Red_Cluster_2.append(red_Wine_3[i])
    elif (label_Red[i] == 3):
        Red_Cluster_3.append(red_Wine_3[i])
    elif (label_Red[i] == 4):
        Red_Cluster_4.append(red_Wine_3[i])
    elif (label_Red[i] == 5):
        Red_Cluster_5.append(red_Wine_3[i])

plt.figure(1)
plt.subplot(211)
plt.scatter(quality,label_Red)
plt.subplot(212)
plt.hist2d(quality,label_Red, bins=3)
plt.show()
