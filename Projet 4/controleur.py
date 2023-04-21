from datetime import timedelta, datetime as dt
from tinydb import Query
import sys

from modele import JoueurModel, TournoiModel, db_joueurs, db_tournois, Tour
from vue import MainView, JoueurView, TournoiView, RapportView
from base import BaseMenu


class JoueurMenu(BaseMenu):
    def __init__(self, modele_objet, vue_objet) -> None:
        super().__init__(modele_objet, vue_objet)


class TournoiMenu(BaseMenu):
    def __init__(self, modele_objet, vue_objet, num_tours=4, tour_actuel=1) -> None:
        super().__init__(modele_objet, vue_objet)
        self.paires = {}
        self.num_tours = num_tours
        self.liste_joueurs = []
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.liste_tours = []
        self.tour_actuel = tour_actuel

    def instruction(self):
        super().instruction()
        if self.option_choisie == "lancement":
            self.lancement()

    def ajouter(self):
        self.lancement()

    def get_liste_joueurs(self):
        self.liste_joueurs = self.instance_vue.ajouter().joueurs

    def nouveau_tour(self, num, liste):
        tour = Tour(num, liste, self.paires, self.scores)
        tour.resultat_tour()
        tour_info = tour.get_tour_info()
        self.liste_tours.append(tour_info)
        return tour_info

    def lancement(self, liste):
        self.set_num_tours()
        for num in range(self.num_tours):
            self.tour_actuel = num
            new_tour = self.nouveau_tour(num, liste)
            new_tour.resultat()

    def set_num_tours(self):
        if self.instance_vue.changer_num_tour() == "oui":
            self.input_data["nombre_tours"] = self.instance_vue.get_num_tours()


# instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
# instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")

# menu_test = BaseMenu(modele_objet=modele_joueur, vue_objet=instance_vue)
# menu_test.instruction()


class RapportMenu:
    def __init__(self) -> None:
        self.option_choisie = ""

    def instruction(self):
        self.option_choisie = RapportView.choix_option(self)

        if self.option_choisie == "liste joueurs":
            self.display_all_joueurs()
        elif self.option_choisie == "liste tournois":
            self.display_all_tournois()
        elif self.option_choisie == "dates tournoi":
            self.display_dates_tournoi()
        elif self.option_choisie == "joueurs tournois":
            self.display_joueurs_tournoi()
        elif self.option_choisie == "rounds tournois":
            self.display_rounds_tournoi()

    def display_all_joueurs(self):
        query_result = db_joueurs.all()
        for joueur in query_result:
            print(
                f"{joueur['identifiant']}. {joueur['prenom'].title()} {joueur['nom'].upper()}"
            )

    def display_all_tournois(self):
        query_result = db_tournois.all()
        for tournoi in query_result:
            print(
                f"{tournoi['identifiant']} (du {tournoi['date_debut']} au {tournoi['date_debut']})"
            )

    def display_dates_tournoi(self, nom_tournoi):
        tournoi = db_tournois.search(Query().nom == nom_tournoi)
        print(
            f"{tournoi['identifiant']} (du {tournoi['date_debut']} au {tournoi['date_debut']})"
        )

    def display_joueurs_tournoi(self, nom_tournoi):
        tournoi = db_tournois.search(Query().nom == nom_tournoi)
        id_joueurs_tournoi = tournoi["joueurs"]
        for id_joueur in id_joueurs_tournoi:
            joueur = db_joueurs.search(Query().identifiant == id_joueur)
            print(f"{joueur['prenom'].title()} {joueur['nom'].upper()}")

    def display_rounds_tournoi(self, nom_tournoi):
        query_result = db_tournois.search(Query().nom == nom_tournoi)
        for tournoi in query_result:
            print(
                f"{tournoi['identifiant']} (du {tournoi['date_debut']} au {tournoi['date_debut']})"
            )

    """def display_all(self, db):
        all_objects = db.all()
        for objet in all_objects:
            print(objet)"""


class Controleur:
    def __init__(self) -> None:
        self.menu = ""

    def execution(self):
        instance_vue_principale = MainView()
        self.menu = instance_vue_principale.choix_menu()
        print(self.menu)

        if self.menu == "joueur":
            modele_joueur = JoueurModel(
                filter_name="identifiant", database_name=db_joueurs
            )
            vue_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=self.menu)
        elif self.menu == "tournoi":
            modele_tournoi = TournoiModel(filter_name="nom", database_name=db_tournois)
            vue_tournoi = TournoiView(labels=TournoiModel, menu_choisi=self.menu)
        elif self.menu == "rapport":
            vue_rapport = RapportView()
        elif self.menu == "quitter":
            sys.exit()


main = Controleur()
main.execution()


# Old tests
"""instance_vue_principale = MainView()
menu = instance_vue_principale.choix_menu()
# instance_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)
# option = instance_joueur.choix_option()
# print(option)

modele_joueur = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
vue_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)

modele_tournoi = TournoiModel(filter_name="nom", database_name=db_tournois)
vue_tournoi = TournoiView(labels=TournoiModel, menu_choisi=menu)"""
