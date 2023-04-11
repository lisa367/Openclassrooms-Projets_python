from datetime import timedelta, datetime as dt

from modele import JoueurModel, instance_modele, Tour, TournoiModel
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



class TournoiMenu(BaseMenu):
    def __init__(self, modele_objet, vue_objet, num_tours=4) -> None:
        super().__init__(modele_objet, vue_objet)
        self.paires = {}
        self.instance_modele.num_tours = num_tours
        self.liste_joueurs = []
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.liste_tours = []

    def get_liste_joueurs(self):
        self.liste_joueurs = self.instance_vue.ajouter().joueurs

    def nouveau_tour(self, num, liste):
        tour = Tour(num, liste, self.paires, self.scores)
        tour.resultat_tour()
        tour_info = tour.get_tour_info()
        self.liste_tours.append(tour_info)
        return tour_info

    def lancement(self, num, liste):
        self.changer_nb_tours()
        for num in range(self.num_tours):
            new_tour = self.nouveau_tour(num, liste)
            new_tour.resultat()

    def changer_nb_tours(self):
        changer_num = input("Voulez-vous changer le nombre de tours (4 par défaut) ? Répondez par oui ou par non : ")
        if changer_num.lower() == "oui":
            self.input_data["nombre_tours"] = input("Veuillez renseigner le nombre de tours: ")



#instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")

menu_test = BaseMenu(modele_objet=instance_modele, vue_objet=instance_vue)
menu_test.instruction()