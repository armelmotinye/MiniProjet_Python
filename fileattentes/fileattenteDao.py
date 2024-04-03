import database
from fileattentes.fileattente import fileattente



class fileattenteDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()
    pass

@classmethod
def ajouter_personne_en_attente(cls, nom):
        # Ajouter une personne à la file d'attente
        connexion = cls.connexion_db()
        cursor = connexion.cursor()
        sql = "INSERT INTO fileattente (nom) VALUES (%s)"
        values = (nom,)
        cls.cursor.execute(sql, values)
        cls.connexion.commit()

@classmethod
def supprimer_personne_de_attente(cls,):
        # Supprimer la première personne de la file d'attente
        connexion = cls.connexion_db()
        cursor = connexion.cursor()
        sql = "SELECT nom FROM fileattente ORDER BY id LIMIT 1"
        cursor.execute(sql)
        personne = cursor.fetchone()
        if personne:
            nom = personne[0]
            print("La première personne de la file d'attente est : ", nom)
            sql_delete = "DELETE FROM fileattente ORDER BY id LIMIT 1"
            cursor.execute(sql_delete)
            connexion.commit()
        else:
            print("La file d'attente est vide.")