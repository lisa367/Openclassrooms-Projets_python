from tinydb import TinyDB, Query
from datetime import timedelta, datetime as dt
from itertools import combinations
import random
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


class Tour:
    def __init__(self, round_num, liste_joueurs, paires_list, scores_dict):
        self.round = round_num
        self.nom = f"Round {self.round}"
        self.liste_joueurs = liste_joueurs
        self.debut = dt.now().strftime("%d/%m/%Y_%H:%M")
        self.fin = ""
        self.matchs = []
        self.paires = paires_list
        self.scores = scores_dict
        # self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.ranking = []
        self.tour_info = {}

    def set_fin_tour(self):
        self.fin = (dt.now() + timedelta(hours=1)).strftime("%d/%m/%Y_%H:%M")
        return self.fin

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

        else:
            ordered_players = [player for player in self.rank()]
            sublists = []
            while len(ordered_players) > 0:
                # if set(self.paires) != set([paire for paire in combinations(self.liste_joueurs, 2)])
                if len(self.paires) != len(
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
        print(
            f"Les paires de joueurs pour les matchs du tour sont les suivantes : {sublists}"
        )
        return sublists

    def resultat_match(self, paire_joueurs):
        match = []
        joueur_1, joueur_2 = paire_joueurs[0], paire_joueurs[1]
        nom_1 = db_joueurs.search(Query().identifiant == joueur_1)[0]
        nom_2 = db_joueurs.search(Query().identifiant == joueur_2)[0]
        print(
            f"Match: {nom_1['prenom'].title()} {nom_1['nom'].upper()} (joueur 1) vs {nom_2['prenom'].title()} {nom_2['nom'].upper()} (joueur 2)"
        )
        match_nul = input("Match nul ? Répondez par oui ou par non :").lower().strip()

        if match_nul == "oui":
            match.append((joueur_1, 0.5))
            match.append((joueur_2, 0.5))
            self.scores[joueur_1] += 0.5
            self.scores[joueur_2] += 0.5

        else:
            gagnant = input(
                "Quel joueur a remporté le match ? Rentrez 1 pour le joueur 1 ou 2 pour le joueur 2 : "
            ).strip()
            while not gagnant.isdigit() and (gagnant == "1" or gagnant == "2"):
                print("Ceci n'est pas une entrée valide.")
                gagnant = input(
                    f"Quel joueur a remporté le match ? Rentrez 1 pour {joueur_1} ou 2 pour {joueur_2}: "
                ).strip()
            score_1 = 1 if int(gagnant) == 1 else 0
            score_2 = 1 if int(gagnant) == 2 else 0
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
        set_paires = self.generation_paires()
        for paire in set_paires:
            self.resultat_match(list(paire))

        self.set_fin_tour()
