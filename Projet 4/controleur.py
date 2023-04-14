from datetime import timedelta, datetime as dt

from modele import JoueurModel, db_joueurs, TournoiModel,db_tournois, Tour
from vue import MainView, JoueurView, TournoiView
from base import BaseMenu



instance_vue = MainView()
menu = instance_vue.choix_menu()
# instance_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)
# option = instance_joueur.choix_option()
# print(option)

modele_joueur = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
vue_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)

modele_tournoi = TournoiModel(filter_name="name", database_name=db_tournois)
vue_tournoi = TournoiView(labels=TournoiModel, menu_choisi=menu)



class JoueurMenu(BaseMenu):
    def __init__(self, modele_objet, vue_objet) -> None:
        super().__init__(modele_objet, vue_objet)


class TournoiMenu(BaseMenu):
    def __init__(self, modele_objet, vue_objet, num_tours=4, tour_actuel=1) -> None:
        super().__init__(modele_objet, vue_objet)
        self.paires = {}
        self.num_tours = num_tours
        self.liste_joueurs = []
        self.scores = {joueur: 0 for joueur in self.liste_joueurs}
        self.liste_tours = []
        self.tour_actuel = tour_actuel

    def instruction(self):
        super().instruction()
        if self.option_choisie == "lancement":
            self.lancement()

    def ajouter(self):
        self.lancement()

    def get_liste_joueurs(self):
        self.liste_joueurs = self.instance_vue.ajouter().joueurs

    def nouveau_tour(self, num, liste):
        tour = Tour(num, liste, self.paires, self.scores)
        tour.resultat_tour()
        tour_info = tour.get_tour_info()
        self.liste_tours.append(tour_info)
        return tour_info

    def lancement(self, liste):
        self.set_num_tours()
        for num in range(self.num_tours):
            self.tour_actuel = num
            new_tour = self.nouveau_tour(num, liste)
            new_tour.resultat()

    def set_num_tours(self):
        if self.instance_vue.changer_num_tour() == "oui":
            self.input_data["nombre_tours"] = self.instance_vue.get_num_tours()



#instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
# instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")

# menu_test = BaseMenu(modele_objet=modele_joueur, vue_objet=instance_vue)
# menu_test.instruction()

