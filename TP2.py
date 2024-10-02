"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 1
Numéro d'équipe :  10
Noms et matricules : Nour Hoballah (2403966 ), Mehdi Chahir (2363286)


########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 
"""

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
            print(f"Le livre {cote_rangement} ---- {bibliotheque[cote_rangement]['Titre']} par {bibliotheque[cote_rangement]['Auteur']} ---- a été ajouté avec succès")
        else:
            print(f"Le livre {cote_rangement} ---- {bibliotheque[cote_rangement]['Titre']} par {bibliotheque[cote_rangement]['Auteur']} ---- est déjà présent dans la bibliothèque")
csvfile.close()



########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

#pour c dans blablabal quand cote starts with S replace with WS
#"WS". Par conséquent, pour tous les livres de l'auteur William Shakespeare, la cote de rangement, qui débute actuellement par "S" suivi de 3 chiffres, devra être modifiée dans le système de gestion par "WS", suivi des mêmes trois chiffres qu'auparavant. (Par exemple, le livre ayant la cote "S028" devra être changé à "WS028"). 

csvfile = open('nouvelle_collection.csv', newline='')
x = csv.DictReader(csvfile)

a = bibliotheque.copy()
for cote_rangement, auteur in a.items():
    if auteur['Auteur'] == "William Shakespeare" and cote_rangement.startswith('S') :
        nouveauCode="WS" + cote_rangement[1:]
        bibliotheque[nouveauCode]=bibliotheque.pop(cote_rangement) # j'updatae la nouvelle version avec pop [nouveauCode] est ma nouvelle cles

print(f' \n Bibliotheque initiale : {bibliotheque} \n')








########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

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

# TODO : Écrire votre code ici






