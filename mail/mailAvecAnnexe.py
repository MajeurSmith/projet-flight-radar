import win32com.client as win32
import os


localPath = os.path.dirname(os.path.abspath(__file__))

def envoieMailAnnexe(destinataire : str, objet : str, txt : str, ):
    """
    destinataire : addresse mail du destinataire au format str
    objet : objet du mail au format str
    txt : texte du mail au format str; possibilité de l'écrire dans le language HTML
    envoie le fichier TableauVol.pdf se trouvant dans le dossier images
    """
    outlook = win32.Dispatch('outlook.application')   # création avec Outlook
    email = outlook.CreateItem(0)                     # Création d'un e-mail
    email.to = destinataire
    email.Subject = objet
    email.HTMLBody = txt
    email.Attachments.Add(localPath + "\..\images\TableauVol.pdf")
    email.Send()
