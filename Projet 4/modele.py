from tinydb import TinyDB, Query
import random
import json


db_joueurs = TinyDB("Databases/joueurs.json")
db_matchs = TinyDB("Databases/matchs.json")
db_tournois = TinyDB("Databases/tournois.json")

query = Query()


class JoueurModel:
    database = db_joueurs
    # headers = ["identifiant", "nom", "prenom", "date_naissance", "score_total", "matchs_total", "matchs_gagnes"]
    headers = ["identifiant", "nom", "prenom", "date_naissance"]

    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.identifiant = data_dict.get("identifiant", "")
        self.nom = data_dict.get("nom", "")
        self.prenom = data_dict.get("prenom", "")
        self.date_naissance = data_dict.get("nom", "")
        self.nombre_matchs_total = 0
        self.nombre_matchs_gagnes = 0
        self.score_total = 0

    def __repr__(self) -> str:
        return f"joueur: {self.prenom} {self.nom} - {self.identifiant}"
    
    def entry_already_exists(self, identifiant):
        db = JoueurModel.database
        id_check = db.search(query["identifiant"] == identifiant)

        return id_check

    def enregistrer(self):
        new_entry = self.data_dict
        JoueurModel.database.insert(new_entry)

        return new_entry

    def modifier(self, filter, value, new_value):
        db = JoueurModel.database
        db.update({filter: new_value}, query[filter] == value)

    def supprimer(self, filter, value):
        db = JoueurModel.database
        db.remove(query[filter] == value)


