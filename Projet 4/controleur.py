from modele import JoueurModel
from vue import View, JoueurView


instance_vue = View()
menu = instance_vue.choix_menu()
instance_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)
option = instance_joueur.choix_option()
# print(option)

if option == "ajouter":
    ex = instance_joueur.ajouter()
elif option == "modifier":
    ex = instance_joueur.modifier()
elif option == "supprimer":
    ex = instance_joueur.supprimer()

print(ex)

class JoueurMenu:
    def __init__(self) -> None:
        self.option_choisie = ""
        self.labels = JoueurModel.headers
        self.instance_joueur = ""

    def instance_joueur(self):
        self.instance_joueur = JoueurView(labels=self.labels, menu_choisi=menu)
        return self.instance_joueur
    
    def choix_option(self):
        self.option_choisie = self.instance_joueur.choix_option()
        return self.option_choisie
    
    def instruction(self):
        if option == "ajouter":
            self.instance_joueur.ajouter()
        elif option == "modifier":
            self.instance_joueur.modifier()
        elif option == "supprimer":
            self.instance_joueur.supprimer()