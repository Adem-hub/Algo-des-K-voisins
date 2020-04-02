import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button




"""
Lancez la fonction Graph() pour creer un graphique aléatoire
"""


def sample():
    new = [ [0,]*2 for _ in range(random.randint(30,110))]
    for i in range (len(new)):
        new[i][0]=random.randint(0,20000)
        new[i][1]=random.randint(0,10000)
        while new[i][0]<new[i][1]:
             new[i][1]=random.randint(0,10000)

    return new





class Knn:


    def __init__(self):

        self.data= sample()
        self.k=random.randrange(4,16,2)
        rd=random.randint(0,len(self.data)-1)
        self.etude = self.data[rd]
        self.genre= self.sexe()
        self.stat= self.etat()



    def donnees(self):
        jean=self.data
        return jean

    def population(self):
        pop=self.etude
        return pop

    def sexe(self):
        self.genre=[]
        for item in self.data:
            p=random.choice(["homme","femme"])
            self.genre.append(p)
        return self.genre

    def etat(self):
        self.stat=[]
        for item in self.data:
            ll=random.choice(["infecté(e)","non infecté(e)"])
            self.stat.append(ll)
        return self.stat

    def NearestNeighbors(self):
        d_voisins=[]
        a=[]

        for index, sample in enumerate(self.data):
            distance= self.dist(sample)
            d_voisins.append((distance, index))
        d_voisins = sorted(d_voisins)
        indice_voisins=[index for distance,index in d_voisins[:self.k]]
        for i in indice_voisins:
            a.append(self.data[i]+ [self.genre[i]]+[self.stat[i]])

        return a



    def dist(self,sample):
        X= sample[0]
        Y= sample[1]
        dist=(X-self.etude[0])**2+(Y-self.etude[1])**2
        dist= np.sqrt(dist)
        return dist







def occurence(population,a):
    L=[]
    Lbis=[]
    sexe=""
    stade=""
    for i in range(len(a)):
        sexe=a[i][2]
        L.append(sexe)
    for j in range(len(a)):
        etat=a[j][3]
        Lbis.append(etat)
    a=L.count('homme')
    b=L.count('femme')
    if b>a:
        sexe="femme"
    else:
        sexe="homme"
    c=Lbis.count('infecté(e)')
    d=Lbis.count('non infecté(e)')
    if c>d:
        stade="infecté(e)"
    else:
        stade="non infecté(e)"
    population.append(sexe)
    population.append(stade)
    return [population,a,b,c,d]





def Graph():
    x=[]
    y=[]
    Echantillon= Knn()
    population= Echantillon.population()
    pop1=population[0]
    pop2=population[1]

    L= Echantillon.donnees()
    for i in range(len(L)):
        x.append(L[i][0])
        y.append(L[i][1])
    normal=plt.scatter(x, y, s=10)

    a= Echantillon.NearestNeighbors()
    del a[0]

###Points sur la figure
    #Voisins
    for i in range(len(a)):
        xx= a[i][0]
        yy=a[i][1]
        if "femme" in a[i]:
            plt.scatter(xx,yy,s=30,color="red")
            if "infecté(e)" in a[i]:
                plt.scatter(xx,yy,s=30,color="red",edgecolors = 'black')

        elif "homme" in a[i]:
            plt.scatter(xx,yy,s=30,color="green")
            if "infecté(e)" in a[i]:
                plt.scatter(xx,yy,s=30, edgecolors = 'black',color="green")


    mp=plt.scatter(pop1,pop2,s=10,color='white')#J'efface le point bleu situé à l'endroit de mon point etudié.
    mp=plt.scatter(pop1,pop2,s=50,color='black',marker = '+', edgecolors = 'black')


    plt.title("Echantillon aléatoire de gens")
    plt.xlabel("x")
    plt.ylabel("y")

    Prediction = occurence(population,a)
    Pr=Prediction[0]
    aa=Prediction[1]
    bb=Prediction[2]
    cc=Prediction[3]
    dd=Prediction[4]


    attributs=str(Pr[2])+", "+str(Pr[3])
##Cercle
    LeCercle= PlusEloigne(a,population)
    circle1 = plt.Circle((population), LeCercle[4], color='red',fill=False, linestyle='--')
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_artist(circle1)
##Legende
    homme=plt.scatter([],[],s=30,color="green")
    femme=plt.scatter([],[],s=30,color="red")
    vide=plt.scatter([],[],s=30,color="white")

    contamine = plt.scatter([],[],s=30,color="white", edgecolors = 'black')
    plt.legend([mp,circle1,homme,femme,contamine,vide,normal],['i̲n̲d̲i̲v̲i̲d̲u̲ ̲é̲t̲u̲d̲i̲é̲: '+ attributs,"K voisins: "+str(len(a)),"homme: "+str(aa),"femme: "+str(bb),"infecté(e): "+str(cc),"non infecté(e): "+str(dd),"population non prise les k voisins"],
              loc = 'upper left', ncol = 1, scatterpoints = 1,
              frameon = True, markerscale = 1, title = 'L͟é͟g͟e͟n͟d͟e͟',
              borderpad = 0.5, labelspacing = 0.5,)

    plt.show()












"""
Cette partie du code sert a trouver le point le plus distant du point choisi afin de trouver le rayon du cercle. On peut faire plus simple avec la classe .
"""

def Cercle(a,pop):
    x1= a[0]
    y1= a[1]
    distance=0
    X= pop[0]
    Y= pop[1]
    distance=(X-x1)**2+(Y-y1)**2
    distance=np.sqrt(distance)
    a.append(distance)
    return a

def PlusEloigne(a,pop):
    d_voisins=[]
    L=[]
    m=0
    z=0
    krk=0
    for index, sample in enumerate(a):
        distance= Cercle(sample,pop)
        d_voisins.append((distance, index))
    d_voisins = sorted(d_voisins)

    indice_voisins=[index for distance,index in d_voisins[:]]

    for i in indice_voisins:
        L.append(a[i])
    for j in range(len(L)):
        r=L[j][4]
        if int(r)>m:
            m=r

    for item in range(len(L)):
        for sousitem in range(len(L[item])):
            kk=L[item][sousitem]
            if m ==kk:
                krk=L[item]

    return krk







