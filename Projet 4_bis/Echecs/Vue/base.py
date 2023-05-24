CHOIX_MENU = """
A: Menu joueur
B: Menu tournoi
C: Menu rapport
D: Quitter
"""


MENU_JOUEUR = """
1: Ajouter un joueur
2: Modifier un profil joueur
3: Supprimer un joueur
"""


MENU_TOURNOI = """
1: Nouveau tournoi
2: Modifier un tournoi
3: Supprimer un tournoi
4: Ajouter un tour
"""

MENU_RAPPORT = """
1: Liste de tous les joueurs
2: Liste de tous les tournois
3: Dates d'un tournoi
4: Joueurs d'un tournoi
5: Rounds et matchs d'un tournoi
"""
menus = {
    "joueur": MENU_JOUEUR,
    "tournoi": MENU_TOURNOI,
    "rapport": MENU_RAPPORT,
    "quitter": "Quitter",
}


class BaseView2:
    def __init__(self, labels, verbose, id_type, menu_choisi) -> None:
        # self.object_name = self.__class__.__name__.strip("View").lower()
        self.object_name = self.__class__.__name__[:-4].lower()
        self.menu_choisi = menu_choisi
        self.options = {1: "ajouter", 2: "modifier", 3: "supprimer"}
        self.labels_list = labels

        formatage_list = [f"{element}:nouvelle_valeur" for element in self.labels_list]
        self.formatage = " ".join(formatage_list)
        self.input_data = {}
        self.new_entry = {}

        self.verbose = verbose
        self.id_type = id_type

    def choix_option(self):
        menu = menus[self.menu_choisi]

        print("Choisissez une des options suivantes : ", menu, "\n")
        reponse = input("Entrez le chiffre de l'option choisie : ")
        print("*" * 15)
        option_choisie = self.options.get(int(reponse), 0)

        return option_choisie

    def input_check(self, data):
        return True

    def get_id(self, instruction):
        object_id = input(
            f"Veuillez renseigner {self.verbose[self.id_type]} du {self.object_name} à {instruction} : "
        )
        # if self.input_check(object_id):
        self.input_data["identifiant"] = object_id
        return object_id

    def get_input_data(self, instruction):
        inputs_raw = input(
            f"Veuillez renseigner les éléments à {instruction} de la manière suivante, séparés d'un espace: {self.formatage}\n"
        )
        inputs_list = [input_data.split(":") for input_data in inputs_raw.split()]

        for item in inputs_list:
            # if self.input_check(input_data[1]):
            self.input_data[item[0]] = item[1]
        return self.input_data

    def ajouter(self):
        for item in self.verbose:
            self.new_entry[item] = input(
                f"Veuillez renseigner {self.verbose[item]} du {self.object_name}: "
            )
        return self.new_entry

    def modifier(self):
        modified_data = {}
        modified_data["filter"] = self.get_id("modifier")
        modified_data["data"] = self.get_input_data("modifier")
        return modified_data

    def supprimer(self):
        identifiant = self.get_id("supprimer")
        return identifiant
