### MENUS ###
from modele import JoueurModel

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

   

class BaseView2:

    def __init__(self, labels, menu_choisi) -> None:
        self.object_name = self.__class__.__name__.strip("View").lower()
        self.menu_choisi = menu_choisi
        self.options = {1: "ajouter", 2: "modifier", 3: "supprimer"}
        self.option_choisie = ""
        self.labels_list = labels

        formatage_list = [f"{element}:nouvelle_valeur" for element in self.labels_list]
        self.formatage = " ".join(formatage_list)
        self.data_dict = {}

    def choix_option(self):
        menu = menus[self.menu_choisi]

        print("Choisissez une des options suivantes : ", menu, "*"*15)
        reponse = input(f"Entrez le chiffre de l'option choisie : ")
        self.option_choisie = self.options.get(int(reponse), 0)

        """if option_choisie:
            self.option_choisie = choix_2
        else:
            print("Veuillez entrer une option valide")"""

        return self.option_choisie
    
    def input_check(self, liste):
        """This method checks if the user input is in the expected data format

        Args:
            liste (dict): Dictionary of the data to check

        Returns:
            bool: The method returns a boolean value
        """
        return True
    
    def get_id(self, instruction):

        object_id = input(f"Veuillez renseigner l'identifiant du {self.object_name} à {instruction} : ")
        # if self.input_check(object_id):
        self.data_dict["identifiant"] = object_id
        
        return object_id

    
    def get_input_data(self, instruction):
        # arguments_dict = {}
        inputs_raw = input(f"Veuillez renseigner les éléments à {instruction} de la manière suivante, séparés d'un espace: {self.formatage}\n")
        inputs_list = [input_data.split(":") for input_data in inputs_raw.split()]
        # print(inputs_list)

        for input_data in inputs_list:
            # if self.input_check(input_data[1]):
            self.data_dict[input_data[0]] = input_data[1]

        #print(self.data_dict)

        return self.data_dict

    
    def delete_object(self):
        object_id = input(f"Veuillez renseigner l'identifiant du {self.object_name} à supprimer :")
        if not self.input_check(object_id):
            object_id = input("Veuillez renseigner un identifiant valide :")
        
        return object_id
    
    def ajouter(self):
        data = self.get_input_data("ajouter")
        return data
    
    def modifier(self):
        new_data = {}
        new_data["filter"] = self.get_id("modifier")
        new_data["data"] = self.get_input_data("modifier")
        return new_data
    
    def supprimer(self):
        identifiant = self.get_id("supprimer")
        return identifiant
    

class JoueurView(BaseView2):
    def __init__(self, labels, menu_choisi) -> None:
        super().__init__(labels, menu_choisi)


instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")