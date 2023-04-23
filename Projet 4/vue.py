### MENUS ###
# from modele import JoueurModel
from base import BaseView2, CHOIX_MENU, MENU_JOUEUR, MENU_TOURNOI, MENU_RAPPORT, menus


class MainView:
    # menus = {"A": MENU_JOUEUR, "B": MENU_TOURNOI, "C": MENU_RAPPORT, "D": "Quitter"}
    cles = {"A": "joueur", "B": "tournoi", "C": "rapport", "D": "quitter"}
    # options = {1: "ajouter", 2: "modifier", 3:"supprimer"}

    def __init__(self) -> None:
        self.menu_choisi = ""

    def choix_menu(self):
        print("Choisissez un des menus suivants : ", CHOIX_MENU, "*" * 15)
        reponse = input("Entrez A, B, C, ou D : ").upper().strip()
        self.menu_choisi = MainView.cles.get(reponse, 0)

        return self.menu_choisi


class JoueurView(BaseView2):
    def __init__(self, labels, menu_choisi) -> None:
        super().__init__(labels, menu_choisi)


class TournoiView(BaseView2):
    def __init__(self, labels, menu_choisi) -> None:
        super().__init__(labels, menu_choisi)

    def choix_option(self):
        self.options[4] = "lancement"
        return super().choix_option()

    def changer_num_tours(self):
        changer_num = input(
            "Voulez-vous changer le nombre de tours (4 par défaut) ? Répondez par oui ou par non : "
        )
        return changer_num.lower().strip()

    def get_num_tours(self):
        num_tour = input("Entrez le nouveau nombre de tours :").strip()
        while not isinstance(num_tour, int):
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

    def choix_option(self):
        print("Choisissez une des options suivantes : ", self.options, "*" * 15)
        reponse = input(f"Entrez le chiffre de l'option choisie : ")
        option_choisie = self.options.get(int(reponse), 0)

        return option_choisie
        # return BaseView2.choix_option(self)
