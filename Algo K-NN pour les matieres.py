import numpy as np
import random
notes=[2,5,10,14,11,13,16,16,17,19,14,18,8,9,12,14]
note=12
k=8


if __name__=='__main__':
    Caracteristiques_du_k()



def dist(note, notes):
    X= notes
    dist=(X-note)**2
    dist= np.sqrt(dist)
    return dist

def NearestNeighbors(note,notes,k):
    d_voisins=[]
    a=[]
    lessts=stats()
    for index, sample in enumerate(notes):
        distance= dist(note,sample)
        d_voisins.append((distance, index))
    d_voisins = sorted(d_voisins)
    indice_voisins=[index for distance,index in d_voisins[:k]]
    for i in indice_voisins:
        a.append([notes[i]]+lessts[i])
    return a

def stats():
    L=[]
    for item in range (len(notes)):
        Mat=["Arts","Ecolo/Agro & Territoires","Hist-géo & Sciences Po","HLP","Langues  étrangères","Mathématiques","NSI","SVT","SI","SES","Physique chimie"]
        New=[]
        for i in range(3):
            l= random.randint(0,len(Mat)-1)
            New.append(Mat[l])
            Mat.pop(l)
        L.append(New)
    return L

def Determine():
    Mat=["Arts","Ecolo/Agro & Territoires","Hist-géo & Sciences Po","HLP","Langues  étrangères","Mathématiques","NSI","SVT","SI","SES","Physique chimie"]
    Dico={}
    Knn=NearestNeighbors(note,notes,k)
    for i in Mat:
        a=0
        for j in range(len(Knn)):
            a+=Knn[j].count(i)
        Dico[i]=a
    for l in Dico.copy():
        if Dico[l]==0:
            Dico.pop(l)

    return Dico

def Caracteristiques_du_k():
    Dico=Determine()
    a=0
    L=[]
    LL=[]
    for values in Dico.values():
        a+=values
    for index,i in enumerate(Dico):
        b= Dico[i]
        Pourcentage= (b*100)/a
        Pourcentage=round(Pourcentage,2)
        L.append((Pourcentage,index))
        print("La probabilité que tu prennes",i,"est de:",Pourcentage,"%")
    L=sorted(L)
    indice_voisins=[index for Pourcentage,index in L[-3:]]
    for k in indice_voisins:
        m=Dico.keys()
        m=list(m)
        LL.append(m[k])
    print()
    print("Tu devrais donc te spécialiser dans: ",LL[0],",ainsi que",LL[1],", et enfin",LL[2])
