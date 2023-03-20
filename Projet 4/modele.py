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
        self.filter = "identifiant"
        
        """self.data_dict = data_dict
        self.identifiant = data_dict.get("identifiant", "")
        self.nom = data_dict.get("nom", "")
        self.prenom = data_dict.get("prenom", "")
        self.date_naissance = data_dict.get("nom", "")
        self.nombre_matchs_total = 0
        self.nombre_matchs_gagnes = 0
        self.score_total = 0

    def __repr__(self) -> str:
        return f"joueur: {self.prenom} {self.nom} - {self.identifiant}" """
    
    def entry_already_exists(self, filter_value, filter="identifant"):
        db = JoueurModel.database
        id_check = db.search(query[filter] == filter_value)

        return id_check

    def enregistrer(self, new_entry):
        # new_entry = self.data_dict
        JoueurModel.database.insert(new_entry)

        return new_entry

    def modifier(self, data_dict, id_value, filter="identifant"):
        db = JoueurModel.database
        # db.update({field: new_value}, query[filter] == value)
        # db.update(data_dict, query[filter] == id_value)
        db.upsert(data_dict, query[filter] == id_value)

    def supprimer(self, filter_value, filter="identifiant"):
        db = JoueurModel.database
        db.remove(query[filter] == filter_value)


ex = {"identifiant": "CCCC", "nom": "Martin", "prenom": "Jean", "date_naissance": "02/04/2009"}
to_modify = ["CCCC", {"prenom": "Julie", "date_naissance": "12/04/2011"}]
instance_modele = JoueurModel()
# instance_modele.enregistrer(ex)
instance_modele.supprimer(filter="prenom", filter_value="Julie")
# instance_modele.modifier(data_dict=to_modify[1], id_value=to_modify[0])