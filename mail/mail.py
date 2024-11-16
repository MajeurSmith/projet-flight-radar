import win32com.client as win32


def envoieMail(txt : str, objet : str, destinataire : str):
    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)
    email.to = destinataire
    email.Subject = objet
    email.HTMLBody=txt
    email.Send()
    print("mail envoyé")
