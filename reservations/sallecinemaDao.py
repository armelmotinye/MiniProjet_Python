import database
from reservations.sallecinema import SalleCinema

class SalleCinemaDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()
pass

@classmethod
def reserver_place(cls, nom, place):
        
        query = "INSERT INTO Reservations (nom, place) VALUES (%s, %s)"
        values = (nom, place)
        cursor.execute(query, values)
        connexion.commit()
        cursor.close()
        db.close()