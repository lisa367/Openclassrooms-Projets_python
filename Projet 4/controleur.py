from modele import JoueurModel, instance_modele
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
    def nouveau_match(self):
        pass

    def nouveau_tour(self):
        pass


#instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)
instance_vue = JoueurView(labels=JoueurModel.headers, menu_choisi="joueur")

menu_test = BaseMenu(modele_objet=instance_modele, vue_objet=instance_vue)
menu_test.instruction()