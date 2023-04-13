### MENUS ###
# from modele import JoueurModel
from base import BaseView2

CHOIX_MENU = """
A: Menu joueur
B: Menu match
C: Menu tournois
D: Menu statistiques
E: Quitter
"""


MENU_JOUEUR = """
1: Ajouter un joueur
2: Modifier un profil joueur
3: Supprimer un joueur
"""

MENU_MATCH = """
1: Nouveau match
2: Afficher les détails d'un match
3: Modifier un match
4: Supprimer un match
"""

MENU_TOURNOI = """
1: Nouveau tournoi
2: Modifier un tournoi
3: Supprimer un tournoi
"""

MENU_STATS = """
1: Liste de tous les joueurs
2: Liste de tous les tournois
3: Dates d'un tournoi
4: Joueurs d'un tournoi
5: Rounds et matchs d'un tournoi
"""
menus = {"joueur": MENU_JOUEUR, "match": MENU_MATCH, "tournoi": MENU_TOURNOI, "rapport": MENU_STATS, "quitter": "Quitter"}

class View:
    menus = {"A": MENU_JOUEUR, "B": MENU_MATCH, "C": MENU_TOURNOI, "D": MENU_STATS, "E": "Quitter"}
    cles = {"A": "joueur", "B": "match", "C": "tournoi", "D": "stats", "E ": "quitter"}
    # options = {1: "ajouter", 2: "modifier", 3:"supprimer"}

    def __init__(self) -> None:
        self.menu_choisi = ''
        self.option_choisie = ''

    def choix_menu(self):
        print("Choisissez un des menus suivants : ", CHOIX_MENU, "*"*15)
        reponse = input("Entrez A, B, C, D ou E : ").upper().strip()
        self.menu_choisi = View.cles.get(reponse, 0)
        # self.menu_choisi = choix_1

        """if choix_1:
            self.menu_choisi = choix_1
        else:
            print("Veuillez entrer une option valide")"""

        return self.menu_choisi

   


    

class JoueurView(BaseView2):
    def __init__(self, labels, menu_choisi) -> None:
        super().__init__(labels, menu_choisi)


class TournoiView(BaseView2):
    def __init__(self, labels, menu_choisi) -> None:
        super().__init__(labels, menu_choisi)
    
    def get_num_tours(self):
        nouveau_num_tour = input("Voulez-vous changer le nombre de tours (4 par defaut) ? [oui/non]:")
        if nouveau_num_tour.lower() == "oui":
            num_tour = input("Entre le nouveau nombre de tours :")
            return int(num_tour)


# instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")