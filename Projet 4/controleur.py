from modele import JoueurModel, instance_modele, MatchModel, TournoiModel
from vue import View, JoueurView
from base import BaseMenu

import random


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
    def __init__(self, num, liste_joueurs):
        self.nom = f"Round {num}"
        self.liste_joueurs = liste_joueurs
        self.debut = ''
        self.fin = ''
        self.matchs = []
        self.paires = {}
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.ranking = []


    def rank(self):
        # self.ranking = sorted(self.scores, key=self.scores.values())
        # print(self.scores)
        self.ranking = sorted(self.scores, key=lambda joueur: self.scores[joueur])
        return self.ranking

class TournoiMenu(BaseMenu):
    def __init__(self, modele_objet, vue_objet, match_objet) -> None:
        super().__init__(modele_objet, vue_objet)
        # self.instance_match = match_objet


    def nouveau_match(self):
        instance_match = ''
        etape_1 = generation_paires(1)
        for set_paire in etape_1:
            paire = list(set_paire)
            resultat_match(paire[0], paire[1])

    def resultat_match(self, joueur_1, joueur_2):
        match = []
        seq = ["nul", "non_nul"]
        resultat = random.choice(seq)
        if resultat == "nul":
            match.append((joueur_1, 0.5))
            match.append((joueur_2, 0.5))
        else:
            seq2 = [0, 1]
            match.append((joueur_1, seq2.pop(random.randint(0,1))))
            match.append((joueur_2, seq2[0]))

        return match

    def nouveau_tour(self):
        pass

    def generation_paires(self, round):
        liste_joueurs = self.liste_joueurs
        if round == 1:
            random.shuffle(liste_joueurs)
            sublists = [set(liste_joueurs[i:i + 2]) for i in range(0, len(liste_joueurs), 2)]
            # self.paires += sublists
        else:
            ordered_players = [player for player in self.rank().keys()]
            sublists = []
            while len(ordered_players) > 0:
                for j in range(1, len(ordered_players)):
                    new_paire = {ordered_players[0], ordered_players[0+j]}
                    if new_paire in self.paires:
                        continue
                    else:
                        sublists.append(new_paire)
                        # self.paires.append(new_paire)
                        ordered_players.pop(j)
                        ordered_players.pop(0)
                        break
                        
        self.paires += sublists
        # return sublists
        return self.paires


#instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")

menu_test = BaseMenu(modele_objet=instance_modele, vue_objet=instance_vue)
menu_test.instruction()