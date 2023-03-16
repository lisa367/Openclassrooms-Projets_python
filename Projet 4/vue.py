### MENUS ###


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

    def choix_option(self, menu_choisi):
        menu = View.menus[menu_choisi]
        options_str = menu.split("\n")
        options = {}

        for item in options_str:
            choix = item.split(": ")
            options[choix[0]] = choix[1]

        n = len(options)
        print("Choisissez une des options suivantes : ", menu, "*"*15)
        reponse = input(f"Entrez le chiffre de l'option choisie : ")
        choix_2 = options.get(reponse, 0)
        self.option_choisie = choix_2

        """if choix_2:
            self.option_choisie = choix_2
        else:
            print("Veuillez entrer une option valide")"""

        return self.option_choisie