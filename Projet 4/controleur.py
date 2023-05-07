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
    def __init__(self, modele_objet, vue_objet, num_tours=4, tour_actuel=0) -> None:
        super().__init__(modele_objet, vue_objet)
        self.paires = {}
        self.nombre_tours = num_tours
        self.liste_joueurs = []
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.dict_tours = {}
        self.date_fin = ""
        self.tour_actuel = tour_actuel

    def execution(self):
        super().execution()
        if self.option_choisie == "ajouter tour":
            self.nouveau_tour()

    def ajouter(self):
        data = self.instance_vue.ajouter()
        data["joueurs"] = data.get("joueurs").strip().split()
        data["nombre_tours"] = self.set_num_tours()
        data["date_fin"] = self.date_fin
        data["tours"] = self.dict_tours
        data["tour_actuel"] = 0
        data["liste_paires"] = {}
        self.instance_modele.enregistrer_db(data)

    def get_liste_joueurs(self):
        self.liste_joueurs = self.instance_vue.ajouter().joueurs

    def nouveau_tour(self, liste):
        # 1. Récupérer les données tournoi à modifier
        id_tournoi = self.instance_vue.get_id("modifier")
        tournoi_all_data = self.instance_modele.retreive_entry_db(id_tournoi)
        tournoi_tours = tournoi_all_data.get("tours")
        num = tournoi_all_data.get("tour_actuel") + 1

        # 2. Récupérer les informations du tour
        tour = Tour(num, liste, self.paires, self.scores)
        tour.resultat_tour()
        tour_info = tour.get_tour_info()

        # 3. Ajouter les info du tour aux données du tournoi
        tournoi_tours[num] = tour_info

        # 4. Enregistrer les modifications
        self.instance_modele.modifier_db(
            data_dict=tournoi_tours, filter_value=id_tournoi
        )

        # 5. Date de fin du tournoi
        if num == tournoi_all_data["nombre_tour"]:
            tournoi_all_data["date_fin"] = tour_info["fin"]

        # 6. Enregistrer le nouveau nombre de tours

        return tour_info
    
    def ajouter_joueurs(self):
        pass

    def set_num_tours(self):
        if self.instance_vue.changer_num_tours() == "oui":
            self.nombre_tours = self.instance_vue.get_num_tours()
        return self.nombre_tours


class RapportMenu:
    def __init__(self, option_choisie) -> None:
        self.option_choisie = option_choisie

    def execution(self):
        # self.option_choisie = RapportView.choix_option(self)

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
                f"{tournoi['nom']} (du {tournoi['date_debut']} au {tournoi['date_fin']})"
            )

    def retreive_tournoi(self):
        rapport_vue = RapportView()
        nom_tournoi = rapport_vue.get_id()
        tournoi = db_tournois.search(Query().nom == nom_tournoi)

        return tournoi[0]

    def display_dates_tournoi(self):
        tournoi = self.retreive_tournoi()
        print(f"{tournoi['nom']} (du {tournoi['date_debut']} au {tournoi['date_fin']})")

    def display_joueurs_tournoi(self):
        tournoi = self.retreive_tournoi()
        joueurs_tournoi = tournoi["joueurs"]
        for id_joueur in joueurs_tournoi:
            joueur_data = db_joueurs.search(Query().identifiant == id_joueur)
            if joueur_data:
                joueur = joueur_data[0]
                print(f"{joueur['prenom'].title()} {joueur['nom'].upper()}")
            else:
                print(
                    f"{id_joueur} : ce joueur n'est pas présent dans la base de données des joueurs. Veuillez créer ce joueur ou modifier l'identifiant renseigné."
                )

    def display_rounds_tournoi(self):
        tournoi = self.retreive_tournoi()
        if tournoi["tours"]:
            for tour in tournoi["tours"].values():
                print(f"{tour['nom']} (du {tournoi['debut']} au {tournoi['fin']})")
        else:
            print("Il n'y a pas encore de tour enregitré pour ce tournoi.")


class Controleur:
    def __init__(self) -> None:
        self.menu = ""

    def execution(self):
        while self.menu != "quitter":
            instance_vue_principale = MainView()
            self.menu = instance_vue_principale.choix_menu()
            # print(f"Menu choisi: {self.menu}")

            if self.menu == "joueur":
                modele_joueur = JoueurModel(
                    filter_name="identifiant", database_name=db_joueurs
                )
                vue_joueur = JoueurView(
                    labels=JoueurModel.headers,
                    verbose=JoueurModel.verbose,
                    id_type=modele_joueur.default_filter,
                    menu_choisi=self.menu,
                )
                # option_choisie = vue_joueur.choix_option()
                menu_joueur = JoueurMenu(
                    modele_objet=modele_joueur, vue_objet=vue_joueur
                )
                menu_joueur.execution()

            elif self.menu == "tournoi":
                modele_tournoi = TournoiModel(
                    filter_name="nom", database_name=db_tournois
                )
                vue_tournoi = TournoiView(
                    labels=TournoiModel.headers,
                    verbose=TournoiModel.verbose,
                    id_type=modele_tournoi.default_filter,
                    menu_choisi=self.menu,
                )
                # option_choisie = vue_tournoi.choix_option()
                menu_tournoi = TournoiMenu(
                    modele_objet=modele_tournoi, vue_objet=vue_tournoi
                )
                menu_tournoi.execution()

            elif self.menu == "rapport":
                vue_rapport = RapportView()
                option_choisie = vue_rapport.choix_option()
                menu_rapport = RapportMenu(
                    option_choisie=option_choisie,
                )
                menu_rapport.execution()

        if self.menu == "quitter":
            sys.exit()


main = Controleur()
main.execution()
