import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

#Recupe de la liste sans doublon
#-------------------------------------------------------------

csvFile = open("Resource/winequality-red.csv", encoding='utf-8')
readFile = list(csv.reader(csvFile, delimiter = ";"))

quality0 = []
quality1 = []
quality2 = []
quality3 = []
quality4 = []
quality5 = []
quality6 = []
quality7 = []
quality8 = []
quality9 = []
quality10 = []


for i in range(1,len(readFile)):
    if readFile[i][11] == "0" :
        quality0.append(i)
    elif readFile[i][11] == "1":
        quality1.append(i)
    elif readFile[i][11] == "2":
        quality2.append(i)
    elif readFile[i][11] == "3":
        quality3.append(i)
    elif readFile[i][11] == "4":
        quality4.append(i)
    elif readFile[i][11] == "5":
        quality5.append(i)
    elif readFile[i][11] == "6":
        quality6.append(i)
    elif readFile[i][11] == "7":
        quality7.append(i)
    elif readFile[i][11] == "8":
        quality8.append(i)
    elif readFile[i][11] == "9":
        quality9.append(i)
    elif readFile[i][11] == "10":
        quality10.append(i)

print("quality 0")
print(len(quality0))
print("quality 1")
print(len(quality1))
print("quality 2")
print(len(quality2))
print("quality 3")
print(len(quality3))
print("quality 4")
print(len(quality4))
print("quality 5")
print(len(quality5))
print("quality 6")
print(len(quality6))
print("quality 7")
print(len(quality7))
print("quality 8")
print(len(quality8))
print("quality 9")
print(len(quality9))
print("quality 10")
print(len(quality10))

csvFile.close()

print()

csvFile = open("Resource/winequality-white.csv", encoding='utf-8')
readFile = list(csv.reader(csvFile, delimiter = ";"))

quality0.clear()
quality1.clear()
quality2.clear()
quality3.clear()
quality4.clear()
quality5.clear()
quality6.clear()
quality7.clear()
quality8.clear()
quality9.clear()
quality10.clear()


for i in range(1,len(readFile)):
    if readFile[i][11] == "0" :
        quality0.append(i)
    elif readFile[i][11] == "1":
        quality1.append(i)
    elif readFile[i][11] == "2":
        quality2.append(i)
    elif readFile[i][11] == "3":
        quality3.append(i)
    elif readFile[i][11] == "4":
        quality4.append(i)
    elif readFile[i][11] == "5":
        quality5.append(i)
    elif readFile[i][11] == "6":
        quality6.append(i)
    elif readFile[i][11] == "7":
        quality7.append(i)
    elif readFile[i][11] == "8":
        quality8.append(i)
    elif readFile[i][11] == "9":
        quality9.append(i)
    elif readFile[i][11] == "10":
        quality10.append(i)

print("quality 0")
print(len(quality0))
print("quality 1")
print(len(quality1))
print("quality 2")
print(len(quality2))
print("quality 3")
print(len(quality3))
print("quality 4")
print(len(quality4))
print("quality 5")
print(len(quality5))
print("quality 6")
print(len(quality6))
print("quality 7")
print(len(quality7))
print("quality 8")
print(len(quality8))
print("quality 9")
print(len(quality9))
print("quality 10")
print(len(quality10))