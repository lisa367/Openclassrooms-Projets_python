from tinydb import TinyDB, Query
from base import BaseModel

db_joueurs = TinyDB("Databases/joueurs.json", indent=4)
db_matchs = TinyDB("Databases/matchs.json", indent=4)
db_tournois = TinyDB("Databases/tournois.json", indent=4)

query = Query()


class JoueurModel(BaseModel):
    database = db_joueurs
    # headers = ["identifiant", "nom", "prenom", "date_naissance", "score_total", "matchs_total", "matchs_gagnes"]
    headers = ["identifiant", "nom", "prenom", "date_naissance"]


class MatchModel(BaseModel):
    headers = ["joueur_1", "score_1", "joueur_2", "score_2"]
    def __init__(self, filter_name, database_name):
        super().__init__(filter_name, database_name)


class Tour:
    def __init__(self, name, liste_joueurs) -> None:
        self.name = name
        self.liste_joueurs = liste_joueurs
        self.debut = ''
        self.fin = ''

class TournoiModel(BaseModel):
    headers = ["nom", "lieu", "date_debut", "date_fin", "nombre_tours", "liste_joueurs"]
    def __init__(self, filter_name, database_name, num_tours=4):
        super().__init__(filter_name, database_name)
        self.liste_joueurs = []
        self.num_tours = num_tours
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.liste_tours = {}
        self.paires = {}

    def lancement(self):
        for num in self.num_tours:
            self.nouveau_tour(num)

    def nouveau_tour(self, num):
        pass

    

instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
modele_tournoi = TournoiModel(filter_name="name", database_name=db_tournois)