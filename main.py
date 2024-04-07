from personnes.listepersonneDao import ListePersonneDao
from fileattentes.fileattenteDao import FileAttenteDao
from reservations.sallecinemaDao import SalleCinemaDao
from personnes.listepersonne import ListePersonne
from fileattentes.fileattente import FileAttente
from reservations.sallecinema import SalleCinema


    # Test de la classe ListePersonneDao

per1 = listepersonne("Armel", 40)
listepersonne.ajouter_personne(per1)
listepersonne.afficher_personnes()
    
     # Test de la classe ListeAttenteDao

attente1 = listeattente("Joel")
fileattente.ajouter_personne_en_attente(attente1)
fileattente.supprimer_personne_de_attente()
    
# Initialisation de la classe SalleCinemaDAO
SalleCinemaDAO.init()

salle = SalleCinema("Salle 1", 100)

nom = input("Entrez le nom de la personne : ")
place = int(input("Entrez le numéro de la place à réserver : "))

SalleCinemaDao.reserver_place(nom, place)
print("Réservation effectuée avec succès.")