from tinydb import TinyDB, Query
from vue import MENU_JOUEUR, MENU_MATCH, MENU_TOURNOI, MENU_STATS


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





menus = {"joueur": MENU_JOUEUR, "match": MENU_MATCH, "tournoi": MENU_TOURNOI, "rapport": MENU_STATS, "quitter": "Quitter"}

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
        """Asks for the user to enter an id

        Args:
            instruction (str): Indicates what action the input will be used for

        Returns:
            str: The identifier of the data to search in the database
        """

        object_id = input(f"Veuillez renseigner l'identifiant du {self.object_name} à {instruction} : ")
        # if self.input_check(object_id):
        # self.data_dict["identifiant"] = object_id
        
        return object_id

    
    def get_input_data(self, instruction):
        inputs_raw = input(f"Veuillez renseigner les éléments à {instruction} de la manière suivante, séparés d'un espace: {self.formatage}\n")
        inputs_list = [input_data.split(":") for input_data in inputs_raw.split()]
        
        for input_data in inputs_list:
            # if self.input_check(input_data[1]):
            self.data_dict[input_data[0]] = input_data[1]
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



class BaseMenu:
    def __init__(self, modele_objet, vue_objet) -> None:
        self.instance_modele = modele_objet
        self.instance_vue = vue_objet

    def instruction(self):
        option_choisie = self.instance_vue.choix_option()

        if option_choisie == "ajouter":
            self.ajouter()
        elif option_choisie == "modifier":
            self.modifier()
        elif option_choisie == "supprimer":
            self.supprimer()
        # elif option_choisie == "afficher-tout":
            # self.afficher_tout()

    
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