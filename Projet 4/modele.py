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

    def entry_already_exists(self, identifiant):
        db = JoueurModel.database
        id_check = db.search(query["identifiant"] == identifiant)

        return id_check

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
        return f"{self.prenom} {self.nom} - {self.identifiant}"

    def enregistrer(self):
        new_entry = {}
        for header in JoueurModel.headers:
            attr = f"{header}"
            new_entry[header] = getattr(self, attr)

        JoueurModel.database.insert(new_entry)

    def enregistrer_2(self):
        new_entry = self.__dict__
        JoueurModel.database.insert(new_entry)

        return new_entry

    def modifier(self, filter, value, new_value):
        db = JoueurModel.database
        db.update({filter: new_value}, query[filter] == value)

    def supprimer(self, filter, value):
        db = JoueurModel.database
        db.remove(query[filter] == value)


class TournoiModel:
    database = db_tournois
    headers = []

    def __init__(self, nom, lieu, date_debut, date_fin, tour_actuel, nombre_tours=4):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.tour_actuel = tour_actuel
        self.liste_tours = []
        self.liste_joueurs = []
        self.nombre_tours = nombre_tours

    def generation_paires(self):
        max_tours = self.nombre_tours
        paires = [random.shuffle(self.liste_joueurs)]
        return paires
    
    def entry_already_exists(self, nom):
        db = TournoiModel.database
        id_check = db.search(query["nom"] == nom)

        return id_check

    def enregistrer(self):
        new_entry = {}
        for header in TournoiModel.headers:
            attr = f"{header}"
            new_entry[header] = attr

        TournoiModel.database.insert(new_entry)

        return new_entry

    def modifier(self, filter, value, new_value):
        db = TournoiModel.database
        db.update({filter: new_value}, query[filter] == value)

    def supprimer(self, filter, value):
        db = TournoiModel.database
        db.remove(query[filter] == value)


class MatchModel:
    database = db_matchs

    def __init__(self, joueur1, joueur2, date_heure_debut, date_heure_fin, id=0):
        self.id = id
        self.nom = "Round"
        self.joueur1 = joueur1
        self.joureur2 = joueur2
        self.score1 = 0
        self.score2 = 0
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.winner = ''
        self.loser = ''

    def __repr__(self) -> str:
        return f"[({self.joueur1}, {self.score1}), ({self.joueur2}, {self.score2})]"

    def id_match(self):
        pass

    def enregistrer(self):
        new_entry = {}
        for header in MatchModel.headers:
            attr = f"{header}"
            new_entry[header] = attr

        MatchModel.database.insert(new_entry)

    def modifier(self, filter, value, new_value):
        db = MatchModel.database
        db.update({filter: new_value}, query[filter] == value)

    def supprimer(self, filter, value):
        db = MatchModel.database
        db.remove(query[filter] == value)