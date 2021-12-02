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

##----------------------------------- Test divers ----------------------------------------------------##
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
"""red_Wine_3 = []

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
plt.show()"""

#-------------------------------------------------clusterisation 4 --------------------------------------------------

"""red_Wine_4 = []

for i in range(len(red_Wine)):
    red_Wine_4.append([fixed_acidity[i] / 15.9, volatile_acidity[i]/1.58, citric_acid[i], residual_sugar[i]/15.5, density[i], alcohol[i]/14.9])

k_means_Red = cluster.KMeans(n_clusters=5,random_state=0)
k_means_Red.fit(red_Wine_4)
label_Red = k_means_Red.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

for i in range(len(red_Wine_4)):
    if(label_Red[i] == 0):
        Red_Cluster_0.append(red_Wine_4[i])
    elif (label_Red[i] == 1):
        Red_Cluster_1.append(red_Wine_4[i])
    elif (label_Red[i] == 2):
        Red_Cluster_2.append(red_Wine_4[i])
    elif (label_Red[i] == 3):
        Red_Cluster_3.append(red_Wine_4[i])
    elif (label_Red[i] == 4):
        Red_Cluster_4.append(red_Wine_4[i])
    elif (label_Red[i] == 5):
        Red_Cluster_5.append(red_Wine_4[i])

plt.figure(1)
plt.subplot(211)
plt.scatter(quality,label_Red)
plt.subplot(212)
plt.hist2d(quality,label_Red, bins=3)
plt.show()"""

#--------------------- cluster 5 ----------------------------------
#qualité 5 et 6 2 cluter en 0,1 et 3,4

'''red_Wine_5 = []

for i in range(len(red_Wine)):
    red_Wine_5.append([pH[i]/4, alcohol[i]])

k_means_Red = cluster.KMeans(n_clusters=5,random_state=0)
k_means_Red.fit(red_Wine_5)
label_Red = k_means_Red.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

for i in range(len(red_Wine_5)):
    if(label_Red[i] == 0):
        Red_Cluster_0.append(red_Wine_5[i])
    elif (label_Red[i] == 1):
        Red_Cluster_1.append(red_Wine_5[i])
    elif (label_Red[i] == 2):
        Red_Cluster_2.append(red_Wine_5[i])
    elif (label_Red[i] == 3):
        Red_Cluster_3.append(red_Wine_5[i])
    elif (label_Red[i] == 4):
        Red_Cluster_4.append(red_Wine_5[i])
    elif (label_Red[i] == 5):
        Red_Cluster_5.append(red_Wine_5[i])

plt.figure(1)
plt.subplot(211)
plt.scatter(quality,label_Red)
plt.subplot(212)
plt.hist2d(quality,label_Red, bins=3)
plt.show()'''
##---------------------- Fin des test ------------------------##

##--------------------- Résultats gardés --------------------##

#---------------------- cluster 6 -----------------------------

red_Wine_6 = []

for i in range(len(red_Wine)):
    red_Wine_6.append(
      [fixed_acidity[i] , volatile_acidity[i] , citric_acid[i], residual_sugar[i] , chloride[i],
       free_sulfure_dioxyde[i] , total_sulfur_dioxyde[i] , density[i], pH[i] , sulphates[i] ,
       alcohol[i] ])



#----------------- Calcul du Kmeans avec 6 clusters ----------------
k_means_Red = cluster.KMeans(n_clusters=6,random_state=0)
k_means_Red.fit(red_Wine_6)
label_Red = k_means_Red.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

for i in range(len(red_Wine_6)):
    if(label_Red[i] == 0):
        Red_Cluster_0.append(red_Wine_6[i])
    elif (label_Red[i] == 1):
        Red_Cluster_1.append(red_Wine_6[i])
    elif (label_Red[i] == 2):
        Red_Cluster_2.append(red_Wine_6[i])
    elif (label_Red[i] == 3):
        Red_Cluster_3.append(red_Wine_6[i])
    elif (label_Red[i] == 4):
        Red_Cluster_4.append(red_Wine_6[i])
    elif (label_Red[i] == 5):
        Red_Cluster_5.append(red_Wine_6[i])

plt.figure(1)
plt.subplot(211)
plt.title("Kmeans avec 6 clusters")
plt.scatter(quality,label_Red)
plt.subplot(212)
plt.hist2d(quality,label_Red, bins=[6,6])
plt.show()

#---------------------------------------------------------------

#----------------- Calcul des silhouette ----------------------------
print("Calcul de la silhouette")
for k in range(2,11) :
  k_means_Red = cluster.KMeans(n_clusters=k,random_state=0)
  k_means_Red.fit(red_Wine_6)
  label_Red = k_means_Red.labels_

  silhouette_avg = silhouette_score(red_Wine_6, label_Red)
  print(
      "For k = ", k,
    "The average silhouette_score of red wine is :",
    silhouette_avg,
  )
#-------------------------------------------------------------------

#----------------- Calcul du Kmeans avec 2 clusters ----------------
k_means_Red = cluster.KMeans(n_clusters=2,random_state=0)
k_means_Red.fit(red_Wine_6)
label_Red = k_means_Red.labels_

Red_Cluster_0 = []
Red_Cluster_1 = []
Red_Cluster_2 = []
Red_Cluster_3 = []
Red_Cluster_4 = []
Red_Cluster_5 = []

for i in range(len(red_Wine_6)):
    if(label_Red[i] == 0):
        Red_Cluster_0.append(red_Wine_6[i])
    elif (label_Red[i] == 1):
        Red_Cluster_1.append(red_Wine_6[i])
    elif (label_Red[i] == 2):
        Red_Cluster_2.append(red_Wine_6[i])
    elif (label_Red[i] == 3):
        Red_Cluster_3.append(red_Wine_6[i])
    elif (label_Red[i] == 4):
        Red_Cluster_4.append(red_Wine_6[i])
    elif (label_Red[i] == 5):
        Red_Cluster_5.append(red_Wine_6[i])

plt.figure(1)
plt.subplot(211)
plt.title("Kmeans avec 2 clusters")
plt.scatter(quality,label_Red)
plt.subplot(212)
plt.hist2d(quality,label_Red, bins=[2,2])
plt.show()