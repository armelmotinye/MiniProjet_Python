import database
from personnes.listepersonne import listepersonne



class listepersonneDao:
    
    connexion = database.connect_db()
    cursor = connexion.cursor()
pass
    
@classmethod
def ajouter_personne(cls, nom, age):
        # Ajouter une personne à la base de données
        
        connexion = cls.connexion_db()
        cursor = connexion.cursor()
        sql = "INSERT INTO Personnes (nom, age) VALUES (%s, %s)"
        values = (nom, age)
        cursor.execute(sql, values)
        connexion.commit()

@classmethod
def afficher_personnes(cls):
        # Récupérer les détails de toutes les personnes depuis la base de données
        connexion = cls.connexion_db()
        cursor = connexion.cursor()
        sql = "SELECT * FROM Personnes"
        cursor.execute(sql)
        personnes = cursor.fetchall()
        for personne in personnes:
            print(personne)
            
@classmethod
def rechercher_personne(cls, nom):
        # Rechercher une personne par son nom dans la base de données
        connexion = cls.connexion_db()
        cursor = connexion.cursor()
        sql = "SELECT * FROM Personnes WHERE nom = %s"
        cursor.execute(sql, (nom,))
        personne = cursor.fetchone()
        if personne:
            print("Personne trouvée : ", personne)
        else:
            print("Personne non trouvée.")
            
@classmethod
def filtrer_personnes_par_age(cls, min_age, max_age):
        # Filtrer les personnes par âge dans la base de données
        connexion = cls.connexion_db()
        cursor = connexion.cursor()
        sql = "SELECT * FROM Personnes WHERE age BETWEEN %s AND %s"
        cursor.execute(sql, (min_age, max_age))
        personnes = cursor.fetchall()
        for personne in personnes:
            print(personne)