import win32com.client as win32


def envoieMail(txt : str, objet : str, destinataire : str):
    outlook = win32.Dispatch('outlook.application')
    namespace = outlook.GetNamespace('MAPI')
    account = namespace.Folders.Item("axel.chavand@ipsa.fr")
    email.SendUsingAccount = account
    email = outlook.CreateItem(0)
    email.to = destinataire
    email.Subject = objet
    email.HTMLBody=txt


envoieMail("""<p>Ceci est un mail</p>""","TEST","axel.chavand@ipsa.fr")
