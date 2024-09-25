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
bibliotheque={}

# j entre dans le fichier
csvfile = open('collection_bibliotheque.csv', newline='')
c = csv.DictReader(csvfile)
for row in c:
    cote_rangement=row['cote_rangement']
    bibliotheque[cote_rangement]={'Titre':row['titre'],'Auteur':row['auteur'],'Date de Publication':row['date_publication']}
   

csvfile.close()


#print(f' \n Bibliotheque initiale : {bibliotheque} \n')
#print(bibliotheque["H007"])












########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

csvfile = open('nouvelle_collection.csv', newline='')
x = csv.DictReader(csvfile)
for row in x:
    cote_rangement=row['cote_rangement']
    if cote_rangement in bibliotheque:
        if row['titre'] != bibliotheque[cote_rangement]["Titre"]:
            bibliotheque[cote_rangement]={'Titre':row['titre'],'Auteur':row['auteur'],'Date de Publication':row['date_publication']}
            print(f"Le livre {bibliotheque[cote_rangement]} ---- {bibliotheque[cote_rangement]['Titre']} par {bibliotheque[cote_rangement]['Auteur']} ---- a été ajouté avec succès")
        else:
            print(f"Le livre {bibliotheque[cote_rangement]} ---- {bibliotheque[cote_rangement]['Titre']} par {bibliotheque[cote_rangement]['Auteur']} ---- est déjà présent dans la bibliothèque")
csvfile.close()








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






