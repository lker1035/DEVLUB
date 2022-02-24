
# Fonction moyenne en statistique.
from cmath import sqrt


def Moyenne(donnees):
    if type(donnees) == list:
        total=0
        for i in donnees:
            total +=i
        return total/len(donnees)


data = [12,89,16,18,185,416]



# Fonction pour variance en statistique.

def variance(donnees):
    if  type(donnees)==list:
        total=0
        for i in donnees:
            total +=(i - Moyenne(donnees))**2
        
        return total/len(donnees)



def standardDeviation(donnees):
    return sqrt(variance(donnees))