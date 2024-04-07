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

    @places.setter
    def place(self, value):
        self._place = value
