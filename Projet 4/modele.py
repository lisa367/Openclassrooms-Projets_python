from tinydb import TinyDB, Query
import random
import json


db_joueurs = TinyDB("Databases/joueurs.json", indent=4)
db_matchs = TinyDB("Databases/matchs.json", indent=4)
db_tournois = TinyDB("Databases/tournois.json", indent=4)

query = Query()


class JoueurModel:
    database = db_joueurs
    # headers = ["identifiant", "nom", "prenom", "date_naissance", "score_total", "matchs_total", "matchs_gagnes"]
    headers = ["identifiant", "nom", "prenom", "date_naissance"]

    def __init__(self):
        self.data_dict = {}
        self.default_filter = "identifiant"
        self.database = db_joueurs
    
    def entry_already_exists(self, filter_value):
        filter = self.default_filter
        id_check = self.search(query[filter] == filter_value)

        return id_check

    def enregistrer(self, new_entry):
        self.database.insert(new_entry)
        return new_entry

    def modifier(self, data_dict, id_value):
        filter = self.default_filter
        self.database.update(data_dict, query[filter] == id_value)

    def supprimer(self, filter_value):
        filter = self.default_filter
        self.database.remove(query[filter] == filter_value)

    def retreive_all(self):
        print(self.database.all())


# ex1 = {"identifiant": "CCCC", "nom": "Marin", "prenom": "Julie", "date_naissance": "12/08/2007"}
# ex2 = {"identifiant": "DDDD", "nom": "Renault", "prenom": "Zoe", "date_naissance": "21/09/2011"}
# to_modify = ["CCCC", {"nom": "Marin", "prenom": "Julie", "date_naissance": "12/04/2011"}]
instance_modele = JoueurModel()

# instance_modele.enregistrer(ex1)
# instance_modele.enregistrer(ex2)
instance_modele.supprimer(filter_value="DDDD")
# instance_modele.modifier(data_dict=to_modify[1], id_value=to_modify[0])
# instance_modele.retreive_all()