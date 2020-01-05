# -*- coding: utf-8 -*-

# Nom/Name Prénom/Given name Matricule/Student ID
# Rakotobe Joss 20027645

import numpy as np

def subsetsum(p):
    # On trie notre liste sauf p[0] dans p_tri
    p_tri=np.sort(p[1:])
    index=np.argsort(p[1:])
    ordre=np.arange(1,len(p_tri)+1)
    sortie=np.zeros(len(p_tri))

    # Initialisation de la solution finale
    x=np.zeros(len(p_tri))          # les x_i
    S=0                             # la somme des nombres

    #Tant que la liste p_tri n'est pas vide
    while len(p_tri)!=0:
        if S+p_tri[-1]<=p[0]:       # On teste si rajouter le prochain plus grand élément de la liste nous donne toujours une solution
            sortie[index[-1]]=1     # On met à jour x_i
            S+=p_tri[-1]            # On met à jour la nouvelle solution
        p_tri=np.delete(p_tri,-1)   # On supprime l'élément ajouté puisqu'on ne peut utiliser chaque élément qu'au plus une fois.
        index=np.delete(index,-1)   # et son index initial correspondant.
    return sortie                   # On retourne les x_i


p1 = (12012,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192)


p2 = (3210,483,220,470,545,38,682,837,632,390,393,972,284,405,367)


p3 = (886,5,10,25,50,100,200,100,50,25,10,5,10,25,50,100,200,100,50,25,10,5)


p4 = (403,1,2,3,4,5,7,9,11,13,15,18,21,24,27,30,34,38,42,46,50,55,60,65,70,75)


p5 = (21021,435,120,473,350,409,173,456,375,431,457,438,409,411,300,317,152,126,113,225,446,277,303,307,434,247,490,139,452,268,190,421,494,378,154,401,306,163,318,439,140,163,218,176,195,305,361,488,242,318,153,155,244,390,115,101,356,425,196,331,120,194,490,361,419,362,253,278,475,447,336,309,122,103,215,498,224,401,346,268,444,117,403,209,266,476,377,416,499,426,187,480,455,231,300,293,143,247,383,336,450)

print('Les x_i ',subsetsum(p1),' donne une somme de :',np.dot(subsetsum(p1),p1[1:]),'.')
print('Les x_i ',subsetsum(p2),' donne une somme de :',np.dot(subsetsum(p2),p2[1:]),'.')
print('Les x_i ',subsetsum(p3),' donne une somme de :',np.dot(subsetsum(p3),p3[1:]),'.')
print('Les x_i ',subsetsum(p4),' donne une somme de :',np.dot(subsetsum(p4),p4[1:]),'.')
print('Les x_i ',subsetsum(p5),' donne une somme de :',np.dot(subsetsum(p5),p5[1:]),'.')
