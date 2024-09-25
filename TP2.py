"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv


csvfile = open('collection_bibliotheque.csv', newline='')

# make a new variable - c - for Python's DictReader object -
c = csv.DictReader(csvfile)

for row in c:
    print(row['titre']+":" +row['auteur']+","+row['date_publication']+","+row['cote_rangement'])


# save and close the file
csvfile.close()
#print(f' \n Bibliotheque initiale : {bibliotheque} \n')








########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






