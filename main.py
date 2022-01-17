""" Mise en pratique du tuto Python sur Youtube : https://youtu.be/oUJolR5bX6g?list=PLCJ49tqkqxxAWGXWjBw9Fx-to6YJxTe5i
par Jonathan de la chaîne codeavecjonathan """

print("Bienvenue dans le programme Py Access")

# Déclaration des variables

prenom1 = input("Quel est votre prénom ? ")
age1 = input("Bonjour, " + prenom1 + ", quel âge avez-vous ? ")
try:
    age_n = int(age1) + 1
except:
    print("ERREUR : Vous devez rentrer votre âge au format nombre.")
else:
    charge = 0
    while charge <= 100:
        print("Chargement en cours " + str(charge) + "%")
        charge = charge + 13
    print("Chargement terminé")
    print("Votre prénom est " + prenom1 + ", vous avez " + str(age1) + " ans.")
    print("L'an prochain, vous aurez " + str(age_n) + " ans.")
