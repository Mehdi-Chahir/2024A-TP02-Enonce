"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 1
Numéro d'équipe :  10
Noms et matricules : Nour Hoballah (2403966 ), Mehdi Chahir (2363286)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : 
import csv
bibliotheque={}
csvfile = open('collection_bibliotheque.csv', newline='')
c = csv.DictReader(csvfile)
for row in c:
    cote_rangement=row['cote_rangement']
    bibliotheque[cote_rangement]={'Titre':row['titre'],'Auteur':row['auteur'],'Date de Publication':row['date_publication']}
   

csvfile.close()
print(f' \n Bibliotheque initiale : {bibliotheque} \n')

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
            print(f"Le livre {cote_rangement} ---- {bibliotheque[cote_rangement]['Titre']} par {bibliotheque[cote_rangement]['Auteur']} ---- a été ajouté avec succès")
        else:
            print(f"Le livre {cote_rangement} ---- {bibliotheque[cote_rangement]['Titre']} par {bibliotheque[cote_rangement]['Auteur']} ---- est déjà présent dans la bibliothèque")
csvfile.close()



########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 
# TODO :
csvfile = open('nouvelle_collection.csv', newline='')
x = csv.DictReader(csvfile)
a = bibliotheque.copy()
for cote_rangement, auteur in a.items():
    if auteur['Auteur'] == "William Shakespeare" and cote_rangement.startswith('S') :
        nouveauCode="WS" + cote_rangement[1:]
        bibliotheque[nouveauCode]=bibliotheque.pop(cote_rangement) # j'updatae la nouvelle version avec pop [nouveauCode] est ma nouvelle cles

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')




########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 
# TODO :
csvfile = open('emprunts.csv', newline='')
x = csv.DictReader(csvfile)
for row in x:
        cote_rangement = row['cote_rangement']
        if cote_rangement in bibliotheque:
            bibliotheque[cote_rangement]['emprunts'] = 'emprunté'
            bibliotheque[cote_rangement]['date_emprunt'] = row['date_emprunt']

for cote, details in bibliotheque.items():
    if 'emprunts' not in details:
        bibliotheque[cote]['emprunts'] = 'disponible'
        bibliotheque[cote]['date_emprunt'] = None

print(f'\n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')
csvfile.close()

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 
# TODO : 
from datetime import datetime
from datetime import timedelta

delai_retour = timedelta(days=30)
frais_par_retard = 2
frais_max = 100
livres_perdus = []
date_aujourd_hui = datetime.now()

for cote, details in bibliotheque.items():
    if details.get('emprunts') == 'emprunté' and details.get('date_emprunt'):
        date_emprunt = datetime.strptime(details['date_emprunt'], '%Y-%m-%d')
        jours_retard = (date_aujourd_hui - date_emprunt).days - delai_retour.days
        
        if jours_retard > 0:
            frais_retard =str(min(jours_retard * frais_par_retard, frais_max)) +"$"
            bibliotheque[cote]['frais_retard'] = frais_retard   

        if jours_retard > 365:
                livres_perdus.append(cote)
                bibliotheque[cote]['livres_perdus'] = "Oui"
        elif jours_retard <= 365:
            livres_perdus.append(cote)
            bibliotheque[cote]['livres_perdus'] = "Non"
    else:
         bibliotheque[cote]['livres_perdus'] = "Non"
         
print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')


