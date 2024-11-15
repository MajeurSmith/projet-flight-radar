import hashlib

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

def fichier(n : str) -> list:                     ### FONCTION QUI ENRENGISTRE DANS UNE LISTE LE CONTENU D'UN FICHIER .txt
    """
    n : nom du fihier sous forme de chaîne de caractères
    renvoie une liste de liste contenant les infos stockées dans le fichier .txt
    """
    f=open(n,"r+")
    donne=f.readlines()
    dico=[]
    for element in donne:
        element=element.rstrip("\n")
        ligne=element.split("\t")
        dico.append(ligne)
    f.close()
    return(dico)

def ouverture(f : str):                            ### FONCTION QUI OUVRE LE FICHIER F 
    """
    f : nom du fichier sous forme de chaîne de caractères
    ouvre le fichier avec la permission d'écrire
    """
    return(open(f,"w+"))

def arret(d : list,f):                              ### FONCTION QUI ECRIT LES CONTENUS D'UNE LISTE DE LISTE DANS UN FICHIER.TXT
    """
    d : liste de liste contenant les infirmations à écrire dans le fichier f
    ferme le fichier f
    """
    for i in range(len(d)):
        f.write(d[i][0]+"\t"+d[i][1]+"\t"+d[i][2])
        f.write("\n")
    f.close()

def ajouterCompte(liste : list, compte : list)->list:
    liste.append(compte)

def modifierCompte(indiceCompte : int, indiceElement : int, nouveauElement, liste :list)->list:
    liste[indiceCompte][indiceElement]=nouveauElement

def supprimerCompte(compte : list, liste : list)->list:
    liste.remove(compte)

def standardText(txt : str)->str:
    return(txt.strip())
