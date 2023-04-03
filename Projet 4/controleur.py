from datetime import timedelta, datetime as dt
from itertools import combinations
import random

from modele import JoueurModel, instance_modele, MatchModel, TournoiModel
from vue import View, JoueurView
from base import BaseMenu



instance_vue = View()
menu = instance_vue.choix_menu()
# instance_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)
# option = instance_joueur.choix_option()
# print(option)

class JoueurMenu:
    def __init__(self) -> None:
        self.option_choisie = ""
        self.labels = JoueurModel.headers
        self.instance_joueur = ""
        self.instance_modele = JoueurModel()

    def instance_joueur(self):
        self.instance_joueur = JoueurView(labels=self.labels, menu_choisi=menu)
        return self.instance_joueur
    
    def choix_option(self):
        self.option_choisie = self.instance_joueur.choix_option()
        return self.option_choisie
    
    def instruction(self):
        if self.option == "ajouter":
            self.ajouter_db()
        elif self.option == "modifier":
            self.modifier_db()
        elif self.option == "supprimer":
            self.supprimer_db()

    def ajouter_db(self):
        new_entry = self.instance_joueur.ajouter()
        self.instance_modele.enregistrer(new_entry=new_entry)

    def modifier_db(self, filter, data):
        new_entry = self.instance_joueur.modifier()
        id=new_entry["filter"]
        self.instance_modele.modifier(value=id)

    def supprimer_db(self):
        entry = self.instance_joueur.supprimer()
        self.instance_modele.supprimer(filter="identifiant", value=entry)


class Tour:
    def __init__(self, round_num, liste_joueurs):
        self.round = round_num
        self.nom = f"Round {self.round}"
        self.liste_joueurs = liste_joueurs
        self.debut = dt.now().strftime("%d/%m/%Y_%H:%M")
        self.fin = (dt.now() + timedelta(hours = 4)).strftime("%d/%m/%Y_%H:%M")
        self.matchs = []
        self.paires = {}
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.ranking = []


    def rank(self):
        self.ranking = sorted(self.scores, key=lambda joueur: self.scores[joueur])
        return self.ranking
    
    def generation_paires(self):
        liste_joueurs = self.liste_joueurs
        if self.round == 1:
            random.shuffle(liste_joueurs)
            sublists = [set(liste_joueurs[i:i + 2]) for i in range(0, len(liste_joueurs), 2)]
            # self.paires += sublists

        else:
            ordered_players = [player for player in self.rank()]
            sublists = []
            while len(ordered_players) > 0 and (self.paires != [set(paire) for paire in combinations(self.liste_joueurs, 2)]):
                for j in range(1, len( ordered_players)):
                    new_paire = {ordered_players[0], ordered_players[0+j]}
                    if new_paire in self.paires:
                        continue
                    else:
                        sublists.append(new_paire)
                        ordered_players.pop(0+j)
                        ordered_players.pop(0)
                        break

        self.paires.extend(sublists)
        return sublists
    
    

class TournoiMenu(BaseMenu):
    def __init__(self, modele_objet, vue_objet, match_objet) -> None:
        super().__init__(modele_objet, vue_objet)
        # self.instance_match = match_objet

    def nouveau_tour(self):
        pass



#instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")

menu_test = BaseMenu(modele_objet=instance_modele, vue_objet=instance_vue)
menu_test.instruction()