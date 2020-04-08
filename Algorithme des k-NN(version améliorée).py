import numpy as np
import random
import matplotlib.pyplot as plt


def sample():
    new = [ [0,]*2 for _ in range(random.randint(30,110))]
    for i in range (len(new)):
        new[i][0]=random.randint(0,20000)
        new[i][1]=random.randint(0,10000)
        while new[i][0]<new[i][1]:
             new[i][1]=random.randint(0,10000)
    return new

def pt():
    a=random.randint(0,20000)
    b=random.randint(0,10000)
    L=[a,b]
    return L



class Knn:


    def __init__(self):

        self.data= sample()
        self.k=random.randrange(5,16,2)
        rd=random.randint(0,len(self.data)-1)
        self.etude = pt()
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
        for item in range(len(self.data)):
            item=random.choice(["homme","femme"])
            self.genre.append(item)
        return self.genre

    def etat(self):
        self.stat=[]
        for item in range(len(self.data)):
            item=random.choice(["infecté(e)","non infecté(e)"])
            self.stat.append(item)
        return self.stat

    def NearestNeighbors(self):
        d_voisins=[]
        a=[]

        for index, sample in enumerate(self.data):
            distance= self.dist(sample)
            d_voisins.append((distance, index))
        d_voisins = sorted(d_voisins)
        loin= d_voisins[:self.k]
        loin= loin[-1]
        got_it=loin[0]
        indice_voisins=[index for distance,index in d_voisins[:self.k]]
        for i in indice_voisins:
            a.append(self.data[i]+ [self.genre[i]]+[self.stat[i]])

        return [a,got_it]



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
    base= Echantillon.NearestNeighbors()
    a=base[0]
    PlusLoin=base[1]

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


    circle1 = plt.Circle((population), PlusLoin, color='red',fill=False, linestyle='--')
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



if __name__=="__main__":
    Graph()














