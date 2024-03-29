### MENUS ###
# from modele import JoueurModel
from .base import BaseView2, CHOIX_MENU, MENU_JOUEUR, MENU_TOURNOI, MENU_RAPPORT, menus


class MainView:
    # menus = {"A": MENU_JOUEUR, "B": MENU_TOURNOI, "C": MENU_RAPPORT, "D": "Quitter"}
    cles = {"A": "joueur", "B": "tournoi", "C": "rapport", "D": "quitter"}
    # options = {1: "ajouter", 2: "modifier", 3:"supprimer"}

    def __init__(self) -> None:
        self.menu_choisi = ""

    def choix_menu(self):
        print("*" * 15)
        print("Choisissez un des menus suivants : ", CHOIX_MENU, "\n")
        reponse = input("Entrez A, B, C, ou D : ").upper().strip()
        print("*" * 15)
        self.menu_choisi = MainView.cles.get(reponse, 0)

        return self.menu_choisi


class JoueurView(BaseView2):
    def __init__(self, labels, verbose, id_type, menu_choisi) -> None:
        super().__init__(labels, verbose, id_type, menu_choisi)


class TournoiView(BaseView2):
    def __init__(self, labels, verbose, id_type, menu_choisi) -> None:
        super().__init__(labels, verbose, id_type, menu_choisi)

    def choix_option(self):
        self.options[4] = "ajouter tour"
        return super().choix_option()

    def changer_num_tours(self):
        changer_num = input(
            "Voulez-vous changer le nombre de tours (4 par défaut) ? Répondez par oui ou par non : "
        )
        return changer_num.lower().strip()

    def get_num_tours(self):
        num_tour = input("Entrez le nouveau nombre de tours :").strip()
        while not num_tour.isdigit():
            num_tour = input("Veuillez entrer un nombre entier : ").strip()
        return int(num_tour)

    def resultat_matchs(self, tour):
        pass


# instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")


class RapportView:
    def __init__(self) -> None:
        self.options = {
            1: "liste joueurs",
            2: "liste tournois",
            3: "dates tournoi",
            4: "joueurs tournois",
            5: "rounds tournois",
        }
        self.option_choisie = ""
        self.menu_choisi = "rapport"

    def choix_option(self):
        return BaseView2.choix_option(self)

    def get_id(self):
        object_id = input(f"Veuillez renseigner le nom du tournoi : ")
        return object_id
