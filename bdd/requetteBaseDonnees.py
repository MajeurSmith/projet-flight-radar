import firebase_admin
from firebase_admin import credentials, db
import os
import hashlib

localPath = os.path.dirname(os.path.abspath(__file__))
# Initialisation de l'application Firebase
firebase_admin.initialize_app(credentials.Certificate(localPath+'/exemple-a4226-firebase-adminsdk-8einv-0fbbc1bd88.json'), {'databaseURL': 'https://exemple-a4226-default-rtdb.europe-west1.firebasedatabase.app/'})

def hash(password: str) -> str:
    """
    Procédure qui renvoie la chaîne de caractère 'password' encodée
    en sha256 sous la forme d'une chaîne de caractère.

    Args:
        password (str): la chaîne de caractère à encoder

    Returns:
        str: la chaîne de caractère encodée
    """
    ## Précondition (début) ##
    assert(type(password) == str), "Erreur de type pour 'password' (requis: str)"
    ## Précondition (fin) ## 
    ## Encodage de la chaîne de caractère (début) ##
    h = hashlib.new("SHA256") # Choix du type d'encodage
    h.update(password.encode()) # Encodage
    hashedPassword = h.hexdigest() # Conversion en chaîne de caractère
    ## Encodage de la chaîne de caractère (fin) ##
    return(hashedPassword) # Renvoie du mot de passe encodé


def ajouterUtilisateur(nom : str, prenom : str, mail : str, mdp : str, clefApi : str, nbApi : int):
    """
    Ajoute un utilisateur dans la base de données qui a pour clef "comptes"
    """
    try :
        if "@" in mail : 
            # Ajouter un utilisateur
            db.reference('comptes').child(mail.replace(".","")).set({
                'nom': nom,
                'prenom': prenom,
                'mail' : mail,
                'mdp' : mdp,
                'clefApi' : clefApi,
                'nbApi' : nbApi
            })
        else:
            print("mail incorrect")
    except:
        print("connexion internet instable")

def modifierMdpUtilisateur(clefUtilisateur : str, nouveauMdp : str):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur 
    """
    try:
        db.reference('comptes').child(clefUtilisateur).update({
            'mdp': nouveauMdp
        })
    except:
        print("connexion internet instable")

def modifierMailUtilisateur(clefUtilisateur : str, nouveauMail : str):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouveauMail est le nouveau mail
    permet de remplacer la valeur de mail par nouveauMail
    """
    try:
        db.reference('comptes').child(clefUtilisateur).update({
            'mail': nouveauMail
        })
    except:
        print("connexion internet instable")

def modifierClefApiUtilisateur(clefUtilisateur : str, nouvelleClefApi : str):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouveauMdp est le nouveau mdp
    permet de remplacer la valeur de clefApi par nouvelleClefApi
    """
    try:
        db.reference('comptes').child(clefUtilisateur).update({
            'clefApi': nouvelleClefApi
        })
    except:
        print("connexion internet instable")

def modifiernbApi(clefUtilisateur : str, nouvelleValeur : int):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouvelleValeur est la nouvelle valeur
    permet de remplacer la valeur de nbApi par nouvelleValeur
    """
    try:
        db.reference('comptes').child(clefUtilisateur).update({
            'nbApi': nouvelleValeur
        })
    except:
        print("connexion internet instable")

def modifierNom(clefUtilisateur : str, nouveauNom : int):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouvelleValeur est la nouvelle valeur
    permet de remplacer la valeur de nom par nouveauNom
    """
    try:
        db.reference('comptes').child(clefUtilisateur).update({
            'nom': nouveauNom
        })
    except:
        print("connexion internet instable")

def modifierPrenom(clefUtilisateur : str, nouveauPrenom : int):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouvelleValeur est la nouvelle valeur
    permet de remplacer la valeur de prenom par nouveauPrenom
    """
    try:
        db.reference('comptes').child(clefUtilisateur).update({
            'prenom': nouveauPrenom
        })
    except:
        print("connexion internet instable")

def supprimerUtilisateur(clefUtilisateur : str):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    permet de supprimer un utilisateur de la base de données
    """
    try:
        db.reference('comptes').child(clefUtilisateur).delete()
    except:
        print("connexion internet instable")

def lireUtilisateur(clefUtilisateur : str)->dict:
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur 
    """
    try:
        return(db.reference('comptes').child(clefUtilisateur).get())
    except:
        print("connexion internet instable")

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