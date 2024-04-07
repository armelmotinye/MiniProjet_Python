from personnes.listepersonneDao import ListePersonneDao
from fileattentes.fileattenteDao import FileAttenteDao
from reservations.sallecinemaDao import SalleCinemaDao
from personnes.listepersonne import ListePersonne
from fileattentes.fileattente import FileAttente
from reservations.sallecinema import SalleCinema


# Test de la classe ListePersonneDao
liste_personne_dao = ListePersonneDao()
per1 = ListePersonne("Armel", 40)
liste_personne_dao.ajouter_personne(per1)
liste_personne_dao.afficher_personnes()
    
# Test de la classe ListeAttenteDao
liste_attente_dao = ListeAttenteDao()
attente1 = listeattente("Joel")
liste_attente_dao.ajouter_personne_en_attente(attente1)
liste_attente_dao.supprimer_personne_de_attente()

# Initialisation de la classe SalleCinemaDAO

def afficher_menu():
    print("=== Menu ===")
    print("1. Réserver une place")
    print("2. Afficher les places réservées")
    print("3. Afficher le nombre de places disponibles")
    print("4. Filtrer les réservations par personne")
    print("5. Annuler les réservations d'une personne")
    print("6. Quitter")
    print("============")

def reserver_place():
    nom = input("Entrez le nom de la personne : ")
    place = int(input("Entrez le numéro de la place à réserver : "))
    SalleCinemaDao.reserver_place(nom, place)
    print("Réservation effectuée avec succès.")

def afficher_places_reservées():
    SalleCinemaDao.afficher_places_reservées()

def afficher_nombre_places_disponibles():
    salle = SalleCinema("Salle 1", 100)
    places_disponibles = salle.nombre_places_disponibles()
    print(f"Il reste {places_disponibles} places disponibles dans la salle.")

def filtrer_reservations_par_personne():
    nom = input("Entrez le nom de la personne pour filtrer les réservations : ")
    salle = SalleCinema("Salle 1", 100)
    salle.filtrer_reservations_par_personne(nom)

def annuler_reservations_personne():
    nom = input("Entrez le nom de la personne pour annuler les réservations : ")
    SalleCinemaDao.annuler_reservations_par_personne(nom)
    print(f"Réservation de {nom} est annulée.")

def main():
    SalleCinemaDao.init()

    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            reserver_place()
        elif choix == "2":
            afficher_places_reservées()
        elif choix == "3":
            afficher_nombre_places_disponibles()
        elif choix == "4":
            filtrer_reservations_par_personne()
        elif choix == "5":
            annuler_reservations_personne()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")   
    
if __name__ == "__main__":
    main()