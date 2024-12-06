from PyQt5 import uic, QtWidgets


win0 = ""
win1 = ""
win2 = ""
win3 = ""
win4 = ""
win5 = ""
app =  ""


def connexion():   #Ouvre la page de connexion
    global win1

    win1.Id1.setPlaceholderText("Identifiant")
    win1.MDP1.setPlaceholderText("Mot de passe")

#    win1.Connexion1.clicked.connect() #Relier fonction de ton code
    win1.Retour1.clicked.connect(fin_win1)

    win1.show()

def creation():    #Ouvre la page de création de compte
    global win2

    win2.Id2.setPlaceholderText("Identifiant")
    win2.MDP2.setPlaceholderText("Mot de passe")
    win2.Nom2.setPlaceholderText("Nom")
    win2.Prenom2.setPlaceholderText("Prenom")
    win2.Mail2.setPlaceholderText("E-Mail")

#    win2.Connexion2.clicked.connect()   #Relier la fonction
    win2.Annuler2.clicked.connect(fin_win2)

    win2.show()

def suppression():    #Ouvre la page de suppression de compte
    global win3

    win3.Id3.setPlaceholderText("Identifiant")
    win3.MDP3.setPlaceholderText("Mot de passe")

#    win3.Confirmer3.clicked.connect() #Relier fonction de ton code
    win3.Annuler3.clicked.connect(fin_win3)

    win3.show()




def aeroport():    #Ouvre la page d'interface des aéroports
    global win4 , app

    ville = app.sender()                                                       #Place la bonne ville dans le titre
    win4.Titre4.setText(f"Liste des vols opérant depuis {ville.objectName()}")



    numéro_vol1 = [1 , 3 , "cce", 5]   #Ajoute les numéro de vol à la liste départs
#Trouver une façon de récupérer ta liste

    for num in range(len(numéro_vol1)) :
        win4.Liste4_1.addItem(str(numéro_vol1[num]))


    numéro_vol2 = ["chocolat" , "coucou" , "cce", "frr"]  #Ajoute les numéro de vol à la liste arrivées
#trouver une façon de récupérer ta liste

    for num in range(len(numéro_vol2)):
        win4.Liste4_2.addItem(str(numéro_vol2[num]))


    win4.Liste4_1.itemClicked.connect(vol)
    win4.Liste4_2.itemClicked.connect(vol)


    win4.Retour4.clicked.connect(fin_win4)
    win4.show()

def vol(item):
    global win5
    print("vol")

    vol = item.text()                      # Insere le numero de vol dans le titre
    win5.Titre5.setText(f"Voici les informations à propos du vol numéro {vol}.")


#Trouver un moyen de relier les infos
    compagnie = "Air France"
    win5.Compagnie5.setText(str(compagnie))
    avion = "A380"
    win5.Avion5.setText(str(avion))
    piste = "C"
    win5.Piste5.setText(str(piste))
    terminal = 23
    win5.Terminal5.setText(str(terminal))
    porte = 4
    win5.Porte5.setText(str(porte))
    retard = "50min"
    win5.Retard5.setText(str(retard))
    heure = "18H40"
    win5.Heure5.setText(str(heure))


    win5.OK5.clicked.connect(fin_win5)
    win5.show()




def fin_win1():
    win1.close()

def fin_win2():
    win2.close()

def fin_win3():
    win3.close()

def fin_win4():
    win4.Liste4_1.clear()
    win4.Liste4_2.clear()
    win4.close()

def fin_win5():
    win5.close()




def fin_programme():
    win0.close()
    sys.exit()

def debut_programme():
    global win0 , win1 , win2 , win3 , win4 , win5 , app

    app = QtWidgets.QApplication([])
    win0 = uic.loadUi("ui/Carte-V3.ui") # fenêtre principal

    n = 100 # Nombre de tours restants
    win0.NombreDutilisation.setText(f"Il vous reste {n} utilisations")

#Connexion des bouttons
    win0.Connexion.clicked.connect(connexion)
    win0.Quitter.clicked.connect(fin_programme)
    win0.Creation.clicked.connect(creation)
    win0.Suppression.clicked.connect(suppression)

#Connexion des villes :
    win0.Dunkerque.clicked.connect(aeroport)
    win0.Lille.clicked.connect(aeroport)
    win0.Amiens.clicked.connect(aeroport)
    win0.Cherbourg.clicked.connect(aeroport)
    win0.Rouen.clicked.connect(aeroport)
    win0.Caen.clicked.connect(aeroport)
    win0.Le_Havre.clicked.connect(aeroport)
    win0.Paris.clicked.connect(aeroport)
    win0.Reims.clicked.connect(aeroport)
    win0.Nancy.clicked.connect(aeroport)
    win0.Strasbourg.clicked.connect(aeroport)
    win0.Rennes.clicked.connect(aeroport)
    win0.Orleans.clicked.connect(aeroport)
    win0.Nantes.clicked.connect(aeroport)
    win0.Poitiers.clicked.connect(aeroport)
    win0.Dijon.clicked.connect(aeroport)
    win0.Limoges.clicked.connect(aeroport)
    win0.Lyon.clicked.connect(aeroport)
    win0.Clermont_Ferrand.clicked.connect(aeroport)
    win0.Bordeaux.clicked.connect(aeroport)
    win0.Toulouse.clicked.connect(aeroport)
    win0.Montpellier.clicked.connect(aeroport)
    win0.Marseille.clicked.connect(aeroport)
    win0.Ajaccio.clicked.connect(aeroport)
    win0.La_Guadeloupe.clicked.connect(aeroport)
    win0.La_Guyane.clicked.connect(aeroport)
    win0.La_Martinique.clicked.connect(aeroport)
    win0.La_Reunion.clicked.connect(aeroport)



    win1 = uic.loadUi("ui/Page de connexion.ui")  # page de connexion
    win2 = uic.loadUi("ui/Création de compte.ui")  # page de création de compte
    win3 = uic.loadUi("ui/Suppression de compte.ui")  # page de suppression de compte
    win4 = uic.loadUi("ui/Interface aéroport.ui") # fenêtre aéroport
    win5 = uic.loadUi("ui/Infos vols.ui") # page des vols

    win0.show()
    app.exec()

debut_programme()



