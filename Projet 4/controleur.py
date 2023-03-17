from modele import JoueurModel
from vue import View, JoueurView


menu = View.choix_menu()
joueur = JoueurView(labels=JoueurModel.headers, menu_choisi=menu)
option = joueur.choix_option()