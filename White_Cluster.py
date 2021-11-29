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

"""k_means_White = cluster.KMeans(n_clusters=6,random_state=0)
k_means_White.fit(white_wine)
label_White = k_means_White.labels_

White_Cluster_0 = []
White_Cluster_1 = []
White_Cluster_2 = []
White_Cluster_3 = []
White_Cluster_4 = []
White_Cluster_5 = []

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
        White_Cluster_5.append(white_wine[i])"""


"""
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
"""

"""plt.figure(1)
plt.subplot(211)
plt.scatter(quality,label_White)
plt.subplot(212)
plt.hist2d(quality,label_White,bins=6)
plt.show()"""

#---------------------- cluster white ----------------------------


white_Wine_6 = []

for i in range(len(white_wine)):
  # red_Wine_6.append([fixed_acidity[i] / 15.9, volatile_acidity[i]/1.58, citric_acid[i], residual_sugar[i]/15.5, chloride[i], free_sulfure_dioxyde[i]/72, total_sulfur_dioxyde[i]/289, density[i], pH[i]/4, sulphates[i]/2, alcohol[i]/14.9])
  """white_Wine_6.append(
      [fixed_acidity[i] , volatile_acidity[i] , citric_acid[i], residual_sugar[i] , chloride[i],
       free_sulfure_dioxyde[i] , total_sulfur_dioxyde[i] , density[i], pH[i] , sulphates[i] ,
       alcohol[i] ])"""

  white_Wine_6.append(
      [fixed_acidity[i], residual_sugar[i], alcohol[i]])

#ph et alcool ou alcool et acid citrique : cluster en 0 - 0.5
#ph, alcool et acid citrique : cluster en 2.5-3

  # red_Wine_6.append([fixed_acidity[i]])

for k in range(2,11) :
  k_means_white = cluster.KMeans(n_clusters=k,random_state=0)
  k_means_white.fit(white_Wine_6)
  label_white = k_means_white.labels_

  silhouette_avg = silhouette_score(white_Wine_6, label_white)
  print(
      "Pour k = ", k,
    "The average silhouette_score is :",
    silhouette_avg,
  )

k_means_white = cluster.KMeans(n_clusters=2,random_state=0)
k_means_white.fit(white_Wine_6)
label_white = k_means_white.labels_

white_Cluster_0 = []
white_Cluster_1 = []
white_Cluster_2 = []
white_Cluster_3 = []
white_Cluster_4 = []
white_Cluster_5 = []

for i in range(len(white_Wine_6)):
    if(label_white[i] == 0):
        white_Cluster_0.append(white_Wine_6[i])
    elif (label_white[i] == 1):
        white_Cluster_1.append(white_Wine_6[i])
    elif (label_white[i] == 2):
        white_Cluster_2.append(white_Wine_6[i])
    elif (label_white[i] == 3):
        white_Cluster_3.append(white_Wine_6[i])
    elif (label_white[i] == 4):
        white_Cluster_4.append(white_Wine_6[i])
    elif (label_white[i] == 5):
        white_Cluster_5.append(white_Wine_6[i])

plt.figure(1)
plt.subplot(211)
plt.scatter(quality,label_white)
plt.subplot(212)
plt.hist2d(quality,label_white, bins=[2,2])
plt.show()