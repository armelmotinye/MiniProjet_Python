import database
from reservations.sallecinema import SalleCinema

class SalleCinemaDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()
    pass

    @classmethod
    def reserver_place(cls, nom, place):
        places_disponibles = cls.nombre_places_disponibles()
        
    # Ajoutez une vérification dans la méthode reserver_place(nom, place) pour s'assurer qu'il reste des places disponibles

        if places_disponibles > 0:      
            sql = "INSERT INTO Reservations (nom, place) VALUES (%s, %s)"
            cls.connexion.execute_sql(sql, (nom, place))
            print("Réservation effectuée avec succès.")
        else:
            print("Désolé, il n'y a plus de places disponibles.")

    @classmethod
    def afficher_places_reservées(cls):
        sql = "SELECT * FROM Reservations"
        reservations = cls.connexion.fetch_data(query)
        print("Places réservées :")
        for reservation in reservations:
            print(f"Nom : {reservation[0]}, Place : {reservation[1]}")
     
    @classmethod
    def recuperer_reservations(cls):
        sql = "SELECT * FROM Reservations"
        return cls.connexion.fetch_data(sql)     
    
    @classmethod
    def nombre_places_disponibles(cls):
        sql = "SELECT COUNT(*) FROM Reservations"
        reservations = cls.connexion.fetch_data(sql)
        places_occupees = reservations[0][0] if reservations else 0
        places_disponibles = 150 - places_occupees  # Supposons une capacité de 150 places pour la salle
        return places_disponibles  
    
    @classmethod
    def filtrer_reservations_par_personne(cls, nom):
        sql = "SELECT * FROM Reservations WHERE nom = %s"
        reservations_personne = cls.connexion.fetch_data(sql, (nom,))
        if reservations_personne:
            print(f"Réservations pour {nom}:")
            for reservation in reservations_personne:
                print(f"Place : {reservation[1]}")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")
    
    @classmethod
    def annuler_reservations_par_personne(cls, nom):
        sql = "DELETE FROM Reservations WHERE nom = %s"
        cls.connexion.execute_sql(sql, (nom,))   