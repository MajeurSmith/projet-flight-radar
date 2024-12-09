import firebase_admin
from firebase_admin import credentials, db
import os


localPath = os.path.dirname(os.path.abspath(__file__))

# Chemin vers votre fichier de clé privée téléchargé depuis Firebase
cred = credentials.Certificate(localPath+'/exemple-a4226-firebase-adminsdk-8einv-0fbbc1bd88.json')

# Initialiser l'application Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://exemple-a4226-default-rtdb.europe-west1.firebasedatabase.app/'  # Remplacez par l'URL de votre base de données
})

def ajouterUtilisateur(nom : str, prenom : str, mail : str, mdp : str, clefApi : str, nbApi : int):
    """
    faire un check de l'email et hasher le mdp et uniformiser le nom et prenom
    """
    # Référence à la base de données
    ref = db.reference('users')  # "users" est la clé où les données seront stockées

    # Ajouter un utilisateur
    ref.child(mail.replace(".","")).set({
        'nom': nom,
        'prenom': prenom,
        'mail' : mail,
        'mdp' : mdp,
        'clefApi' : clefApi,
        'nbApi' : nbApi
    })

def modifierMdpUtilisateur(clefUtilisateur : str, nouveauMdp : str):
    # Mise à jour d'un utilisateur
    ref = db.reference('users')
    ref.child(clefUtilisateur).update({
        'mdp': nouveauMdp
    })

def modifierMailUtilisateur(clefUtilisateur : str, nouveauMail : str):
    # Mise à jour d'un utilisateur
    ref = db.reference('users')
    ref.child(clefUtilisateur).update({
        'mdp': nouveauMail
    })

def modifierClefApiUtilisateur(clefUtilisateur : str, nouveauMdp : str):
    # Mise à jour d'un utilisateur
    ref = db.reference('users')
    ref.child(clefUtilisateur).update({
        'mdp': nouveauMdp
    })

def modifiernbApi(clefUtilisateur : str, nouvelleValeur : int):
    ref = db.reference('users')
    ref.child(clefUtilisateur).update({
        'nbApi': nouvelleValeur
    })

def supprimerUtilisateur(clefUtilisateur : str):
    ref = db.reference('users')
    # Supprimer un utilisateur
    ref.child(clefUtilisateur).delete()

def lireUtilisateur(clefUtilisateur : str)->dict:
    ref = db.reference('users')
    # Lire les données depuis la base de données
    user_ref = ref.child(clefUtilisateur)
    user_data = user_ref.get()
    return(user_data)

def getNomUtilisateur(utilisateur : dict)->str:
    return utilisateur["nom"]

def getPrenomUtilisateur(utilisateur : dict)->str:
    return utilisateur["prenom"]

def getMailUtilisateur(utilisateur : dict)->str:
    return utilisateur["mail"]

def getMdpUtilisateur(utilisateur : dict)->str:
    return utilisateur["mdp"]

def getClefApiUtilisateur(utilisateur : dict)->str:
    return utilisateur["clefApi"]

def getNbClefApiUtilisateur(utilisateur : dict)->str:
    return utilisateur["nbApi"]


ajouterUtilisateur("c'est titou connard","miammm","test.test@gmail.com","test","test",100)
