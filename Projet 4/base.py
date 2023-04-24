from tinydb import Query

# from vue import MENU_JOUEUR, MENU_TOURNOI, MENU_RAPPORT


query = Query()


class BaseModel:
    def __init__(self, filter_name, database_name):
        self.data_dict = {}
        self.default_filter = filter_name
        self.database = database_name

    def entry_already_exists(self, filter_value):
        id_check = self.database.search(query[self.default_filter] == filter_value)
        if id_check:
            return id_check
        else:
            return None

    def enregistrer_db(self, new_entry):
        if not self.entry_already_exists(new_entry[self.default_filter]):
            self.database.insert(new_entry)
            return new_entry
        else:
            return "Cette entrée existe déjà dans la base de données"

    def modifier_db(self, data_dict, id_value):
        self.database.update(data_dict, query[self.default_filter] == id_value)

    def supprimer_db(self, id_value):
        self.database.remove(query[self.default_filter] == id_value)

    def retreive_all_db(self):
        print(self.database.all())

    def retreive_entry_db(self, filter_value):
        entry = self.database.search(query[self.default_filter] == filter_value)
        return entry


CHOIX_MENU = """
A: Menu joueur
B: Menu tournoi
C: Menu rapport
E: Quitter
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
4: Lancement du tournoi
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
        self.object_name = self.__class__.__name__.strip("View").lower()
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

        print("Choisissez une des options suivantes : ", menu, "*" * 15)
        reponse = input(f"Entrez le chiffre de l'option choisie : ")
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
        for item in self.headers:
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


class BaseMenu:
    def __init__(self, modele_objet, vue_objet) -> None:
        self.instance_modele = modele_objet
        self.instance_vue = vue_objet
        self.option_choisie = ""

    def get_option(self):
        self.option_choisie = self.instance_vue.choix_option()
        return self.option_choisie

    def execution(self):
        self.get_option()

        if self.option_choisie == "ajouter":
            self.ajouter()
        elif self.option_choisie == "modifier":
            self.modifier()
        elif self.option_choisie == "supprimer":
            self.supprimer()

    def ajouter(self):
        data = self.instance_vue.get_input_data("ajouter")
        self.instance_modele.enregistrer_db(data)

    def modifier(self):
        id = self.instance_vue.get_id("modifier")
        new_data = self.instance_vue.get_input_data("modifier")
        self.instance_modele.modifier_db(id_value=id, data_dict=new_data)

    def supprimer(self):
        id = self.instance_vue.get_id("supprimer")
        self.instance_modele.supprimer_db(id_value=id)


# instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
# instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")

# menu_test = BaseMenu(modele_objet=instance_modele, vue_objet=instance_vue)
# menu_test.instruction()
