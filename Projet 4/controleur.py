from modele import JoueurModel
from vue import View, JoueurView


instance_vue = View()
menu = instance_vue.choix_menu()
instance_joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)
option = instance_joueur.choix_option()
# print(option)

if option == "ajouter":
    ex = instance_joueur.ajouter()
if option == "modifier":
    ex = instance_joueur.modifier()
if option == "supprimer":
    ex = instance_joueur.supprimer()

print(ex)