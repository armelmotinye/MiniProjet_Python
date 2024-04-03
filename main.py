from personnes.listepersonneDao import listepersonneDao
from fileattentes.fileattenteDao import fileattenteDao
from personnes.listepersonne import listepersonne
from fileattentes.fileattente import fileattente


    # Test de la classe ListePersonneDao

per1 = listepersonne("Armel", 40)
listepersonne.ajouter_personne(per1)
listepersonne.afficher_personnes()
    
     # Test de la classe ListeAttenteDao

attente1 = listeattente("Joel")
fileattente.ajouter_personne_en_attente(attente1)
fileattente.supprimer_personne_de_attente()
    
