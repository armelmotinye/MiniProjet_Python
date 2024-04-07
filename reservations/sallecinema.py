class SalleCinema:
    def __init__(self, nom_salle, place):
        self._nom_salle = nom_salle
        self._place = place

     
    # Getters et setters

    @property
    def nom_salle(self):
        return self._nom_salle

    @nom_salle.setter
    def nom_salle(self, value):
        self._nom_salle = value

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        self._place = value
        
    def __init__(self, nom_salle, capacite):
        self._salle = salle
        self._capacite = capacite

    @property
    def salle(self):
        return self._salle

    @salle.setter
    def salle(self, value):
        self._salle = value

    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self, value):
        self._capacite = value

    
    def nombre_places_disponibles(self):
        # Supposons que nous ayons une référence à la classe SalleCinemaDao pour récupérer les données de la base de données
        reservations = SalleCinemaDao.recuperer_reservations()
        places_occupees = len(reservations)
        places_disponibles = self._capacite - places_occupees
        return places_disponibles

    