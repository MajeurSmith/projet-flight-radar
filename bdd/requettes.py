import pyodbc
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

def connectionRadar()->object:
    """
    Aucun argument
    Permet de se connecter à la bdd Radar
    Renvoie un truc pratique
    """
    connection = pyodbc.connect("DRIVER={SQL Server};"+
                                "Server=DESKTOP-NC901GH\SQLEXPRESS;"+
                                "Database=bddRadar;"+
                                "Trusted_Connection=True")
    connection.autocommit = True
    return connection

def createTable(table):
    """
    table : truc pratique renvoyé par connectionRadar()
    Crée la table dans la bdd bddRadar
    """
    create_table_sql = '''
    CREATE TABLE Compte (
        ID INT PRIMARY KEY,
        Nom VARCHAR(100),
        Prenom VARCHAR(100),
        Mdp VARCHAR(100),
        Mail VARCHAR(100),
        ClefApi VARCHAR(32),
        NbApi INTEGER,
    )
    '''
    cursor = table.cursor()
    cursor.execute(create_table_sql)
    table.commit()

def ajouterCompte(table, nom : str, prenom : str, mdp : str, mail : str, clefApi : str, NbApi : int):
    """
    table : truc pratique renvoyé par connectionRadar
    id : int ou str; id de l'utilisateur dans la base de données
    nom : str; nom du compte
    prenom : str; prénom du compte
    mdp : str; mdp du compte, il est automatiquement hasher avant d'être enregistré
    """
    table.execute(f"INSERT INTO Compte (Nom, Prenom, Mdp, Mail, ClefApi, NbApi) VALUES ('"+str(nom)+"','"+str(prenom)+"','"+hash(str(mdp))+"','"+str(mail)+"','"+str(clefApi)+"','"+str(NbApi)+"')")

def select(table, mail : str, nameTable : str = "Compte")->tuple:
    cursor = table.cursor()
    cursor.execute(f"SELECT * FROM Compte WHERE Mail = '{mail}';")
    for data in cursor: return data

def supprimerCompte(table, mail : str):
    table.execute(f"DELETE FROM Compte WHERE Mail='{mail}';")

def getNomUtilisateur(utilisateur : tuple):
    return utilisateur[1]

def getPrenomUtilisateur(utilisateur : tuple):
    return utilisateur[2]

def getMdpUtilisateur(utilisateur : tuple):
    return utilisateur[3]

def getMailUtilisateur(utilisateur : tuple):
    return utilisateur[4]

def getKeyApiUtilisateur(utilisateur : tuple):
    return utilisateur[5]

def getNbApi(utilisateur : tuple):
    return utilisateur[6]

