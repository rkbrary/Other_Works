# -*- coding: utf-8 -*-

# Composition de deux fonctions
def compo(f,g):
    return tuple([f[g[i]-1] for i in range(len(f))])    #le -1 est nécessaire car les tableaux sont indexés à partir de 0 et non de 1

# La fonction feature permet de réduire considérablement le temps de calcul dans certains cas (ex : (s5,f5))
# Cette fonction retourne le nombre maximal de répétitions d'un même chiffre.
# L'idée est la suivante, ce nombre ne peut qu'augmenter lorsqu'on applique une autre fonction i.e :
# On a toujours : feature(compo(f,g)) >= feature(g) car les images identiques de g auront une image identique par f (principe d'une fonction).
def feature(f):
    g=[0 for i in range(len(f))]
    for i in range(len(f)):
        g[f[i]-1]+=1
    return max(g)

def composition(s,f):
    n=feature(f)
    s0=set()
    while(s!=s0):
        # On crée une copie de s afin de tester si s suite à l'opération ci-dessous
        s0=s
        # On augmente s de toutes ses multiplications possibles: l'ensemble des compositions entre les éléments de s
        for g in s:
            for h in s:
                x=compo(g,h)
                if feature(x)<=n:
                    s=s|{x}

        #On teste si f est dans s, sinon on continue d'augmenter s si possible
        if f in s:
            return True

    #Rendu ici, s a atteint sa taille maximale, et f n'est toujours pas dans s.
    return False

f11 = tuple([3, 1, 3, 4]) # 1->3 2->1 3->3 4->4
f12 = tuple([3, 4, 2, 1]) # tuples car une liste ne peut pas
s1 = set([f11,f12])       # servir d'élément d'un ensemble
f1 = tuple([1, 1, 1, 2])

f21 = tuple([3, 5, 4, 2, 6, 8, 1, 7])
f22 = tuple([1, 4, 3, 2, 5, 6, 7, 8])
s2 = set([f21,f22])
f2 = tuple([8, 7, 6, 5, 4, 3, 2, 1])

f31 = tuple([3, 3, 4, 4, 5, 5])
f32 = tuple([3, 4, 2, 1, 6, 6])
f33 = tuple([4, 4, 4, 4, 5, 5])
s3 = set([f31,f32,f33])
f3 = tuple([2, 1, 4, 3, 5, 5])

f41 = tuple([1, 2, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12])
f42 = tuple([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])
f43 = tuple([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
s4 = set([f41,f42,f43])
f4 = tuple([2, 1, 4, 3, 5, 7, 7, 7, 7, 7, 7, 7])

f51 = tuple([3, 3, 5, 5, 7, 7, 1, 1, 11, 12, 12, 1])
f52 = tuple([3, 3, 1, 1, 5, 5, 7, 7, 7, 4, 12, 11])
f53 = tuple([1, 1, 3, 3, 5, 5, 9, 7, 9, 9, 10, 12])
s5 = set([f51,f52,f53])
f5 = tuple([7, 7, 3, 3, 1, 1, 5, 5, 12, 11, 10, 4])

f61 = tuple([3, 4, 4, 2, 6, 8, 1, 7, 3])
f62 = tuple([4, 4, 4, 4, 4, 5, 5, 8, 1])
s6 = set([f61,f62])
f6 = tuple([2, 1, 4, 4, 5, 6, 8, 7, 3])

print(composition(s1,f1)) # True
print(composition(s2,f2)) # True
print(composition(s3,f3)) # False
print(composition(s4,f4)) # True (Voir plus bas) Temps de calcul astronomiquement long (après une journée, mémoire saturée)
print(composition(s5,f5)) # False
print(composition(s6,f6)) # False


# 4eme composition à la main:
identity = tuple([i + 1 for i in range(12)])
def power(f,n):
    g=f
    for i in range(n-1):
        g=compo(g,f)
    return g

#fonction permutation de deux éléments
def perm(n,p):
    g=[i+1 for i in range(12)]
    g[n-1],g[p-1]=g[p-1],g[n-1]
    return tuple(g)

#### Il a déjà été montré que f42 et f43 engendre S_12. Donc on sait que toute permutation est dans <s4>.


#faire la composition de tous les éléments d'une liste de fonctions (dans l'ordre de la liste)
def big_compo(F):
    g=identity
    for f in F:
        g=compo(g,f)
    return g

# f43 already permute 1 and 2
# F34 permute 3 and 4
F34=[power(f42,2),f43,power(f42,10)]
# 5 is already fixed

# Now we fixe all the rest to 7:

    # create a function that fix seven consecutives indexes to the same value
fix7=compo(power(f42,11),f41)
for i in range(5):
    fix7=compo(power(f42,11),compo(f41,fix7))

    # change them to 7 and at the right place
fix7=compo(compo(power(f42,4),fix7),power(f42,9))
    # permute the other one to the right one
for i in range(5):
    fix7=compo(perm(i+1,i+8),fix7)

# On compose le tout et on obtient f4
print(big_compo([fix7]+F34+[f43]))
