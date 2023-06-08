from tinydb import TinyDB, Query
from .base import BaseModel

db_joueurs = TinyDB("Databases/joueurs.json", indent=4)
db_tournois = TinyDB("Databases/tournois.json", indent=4)

query = Query()


class JoueurModel(BaseModel):
    database = db_joueurs
    # headers = ["identifiant", "nom", "prenom", "date_naissance", "score_total", "matchs_total", "matchs_gagnes"]
    headers = ["identifiant", "nom", "prenom", "date_naissance"]
    verbose = {
        "identifiant": "l'identifiant",
        "nom": "le nom",
        "prenom": "le prénom",
        "date_naissance": "la date de naissance",
    }

    def __repr__(self, joueur_object):
        return f"{joueur_object['identifiant']}. {joueur_object['prenom'].title()} {joueur_object['nom'].upper()}"


class TournoiModel(BaseModel):
    headers = [
        "nom",
        "lieu",
        "date_debut",
        "date_fin",
        "nombre_tours",
        "tours",
        "tour_actuel",
        "joueurs",
        "description",
        "liste_paires",
        "scores",
    ]
    verbose = {
        "nom": "le nom",
        "lieu": "le lieu",
        "date_debut": "la date de début",
        "joueurs": "la liste des joueurs",
        "description": "une description (optionnel)",
    }

    def __init__(self, filter_name, database_name, num_tours=4):
        super().__init__(filter_name, database_name)
        self.liste_joueurs = []
        self.num_tours = num_tours
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.resultats_tours = {}
        self.paires = {}

    def __repr__(self, tournoi_object) -> str:
        return f"{tournoi_object['identifiant']} (du {tournoi_object['date_debut']} au {tournoi_object['date_debut']})"
