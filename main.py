"""Formation apprendre la programmation python depuis Youtube
https://www.youtube.com/watch?v=oUJolR5bX6g&list=PLCJ49tqkqxxAWGXWjBw9Fx-to6YJxTe5i
"""

# Définition des fonctions
# Fonction pour demander l'âge
def demander_age(nom_personne):
    # Définition de la variable âge en nombre avec boucle de vérification que l'utilisateur rentre bien un âge
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel âge avez-vous ? ")
        try:
            age_int = int(age_str)
        # Réponse affichée si l'utilisateur rentre autre chose que des nombres
        except:
            print("ERREUR : Vous devez renseigner uniquement un nombre pour l'âge, les lettres et autres caractères ne sont pas autorisés")
        return age_int
    # Fin de la boucle de vérification de l'âge


#Fonction pour demander le prénom de l'utilisateur
def demander_prenom():
    reponse_prenom = ""
    while reponse_prenom == "":
        reponse_prenom = input("Quel est votre prénom ? ")
    return reponse_prenom


#Fonction pour afficher les informations de la personnes
def afficher_informations_personne(nom, age):
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    #Conditions pour afficher un texte en fonction de l'âge
    if age <= 10:
        print("Vous êtes un enfant")
    elif age == 18:
        print("Félicitation, vous êtes tout juste majeur")
    elif age >= 60:
        print("Vous êtes senior")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
    print("L'année prochaine vous aurez " + str(age+1) + " ans")


# Appel de la fonction pour demander le prénom
prenom1 = demander_prenom()
prenom2 = demander_prenom()

# Appel de la fonction pour demander l'âge
age1 = demander_age(prenom1)
age2 = demander_age(prenom2)

# Afficher les résultats dans la console
afficher_informations_personne(prenom1, age1)
afficher_informations_personne(prenom2, age2)

#Déclaration de la variable du mot de passe
mot_de_passe = ""

#Boucle mot de passe
while not mot_de_passe == "shibboleth":
    mot_de_passe = input("Quel est le mot de passe des hommes de Guiléad pour passer le Jourdain? ")
    if mot_de_passe == "shibboleth":
        print("Accès autorisé, vous pouvez traverser le Jourdain")
    else:
        print("Accès refusé, relisez votre Bible en Juges au chapitre 12, verset 4 à 6.")

