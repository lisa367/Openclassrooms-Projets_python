from tinydb import TinyDB, Query
from datetime import timedelta, datetime as dt
from itertools import combinations
import random
from base import BaseModel

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

    def __repr__(self, joueur):
        return f"{joueur['identifiant']}. {joueur['prenom'].title()} {joueur['nom'].upper()}"


class MatchModel(BaseModel):
    headers = ["joueur_1", "score_1", "joueur_2", "score_2"]

    def __init__(self, filter_name, database_name):
        super().__init__(filter_name, database_name)


class TournoiModel(BaseModel):
    headers = ["nom", "lieu", "date_debut", "date_fin", "nombre_tours", "joueurs"]
    verbose = {
        "nom": "le nom",
        "lieu": "le lieu",
        "debut": "la date de début",
        "fin": "la date de fin",
        "joueurs": "la liste de joueurs",
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


class Tour:
    def __init__(self, round_num, liste_joueurs, paires_dict, scores_dict):
        self.round = round_num
        self.nom = f"Round {self.round}"
        self.liste_joueurs = liste_joueurs
        self.debut = dt.now().strftime("%d/%m/%Y_%H:%M")
        self.fin = (dt.now() + timedelta(hours=1)).strftime("%d/%m/%Y_%H:%M")
        self.matchs = []
        self.paires = paires_dict
        self.scores = scores_dict
        self.ranking = []
        self.tour_info = {}

    def rank(self):
        self.ranking = sorted(self.scores, key=lambda joueur: self.scores[joueur])
        return self.ranking

    def generation_paires(self):
        liste_joueurs = self.liste_joueurs
        if self.round == 1:
            random.shuffle(liste_joueurs)
            sublists = [
                set(liste_joueurs[i : i + 2]) for i in range(0, len(liste_joueurs), 2)
            ]
            # self.paires += sublists

        else:
            ordered_players = [player for player in self.rank()]
            sublists = []
            while len(ordered_players) > 0:
                if set(self.paires) != set(
                    [paire for paire in combinations(self.liste_joueurs, 2)]
                ):
                    for j in range(1, len(ordered_players)):
                        new_paire = {ordered_players[0], ordered_players[0 + j]}
                        if new_paire in self.paires:
                            continue
                        else:
                            sublists.append(new_paire)
                            ordered_players.pop(0 + j)
                            ordered_players.pop(0)
                            break
                else:
                    ordered_players = []

        self.paires.extend(sublists)
        return sublists

    def resultat_match(self, joueur_1, joueur_2):
        match = []
        seq = ["nul", "non_nul"]
        resultat = random.choice(seq)
        if resultat == "nul":
            match.append((joueur_1, 0.5))
            match.append((joueur_2, 0.5))
            self.scores[joueur_1] += 0.5
            self.scores[joueur_2] += 0.5

        else:
            seq2 = [0, 1]
            score_1 = seq2.pop(random.randint(0, 1))
            score_2 = seq2[0]
            match.append((joueur_1, score_1))
            match.append((joueur_2, score_2))
            self.scores[joueur_1] += score_1
            self.scores[joueur_2] += score_2

        self.matchs.append(match)
        # print(match)
        return match

    def get_tour_info(self):
        self.tour_info["nom"] = self.nom
        self.tour_info["debut"] = self.debut
        self.tour_info["fin"] = self.fin
        self.tour_info["matchs"] = self.matchs

        return self.tour_info

    def resultat_tour(self):
        paires = self.generation_paires()
        for paire in list(paires):
            self.resultat_match(paire[0], paire[1])


# modele_joueur = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
# modele_tournoi = TournoiModel(filter_name="name", database_name=db_tournois)
