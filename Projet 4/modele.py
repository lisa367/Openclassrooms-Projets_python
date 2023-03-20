from tinydb import TinyDB, Query
from base import BaseModel

db_joueurs = TinyDB("Databases/joueurs.json", indent=4)
db_matchs = TinyDB("Databases/matchs.json", indent=4)
db_tournois = TinyDB("Databases/tournois.json", indent=4)

query = Query()


class JoueurModel(BaseModel):
    database = db_joueurs
    # headers = ["identifiant", "nom", "prenom", "date_naissance", "score_total", "matchs_total", "matchs_gagnes"]
    headers = ["identifiant", "nom", "prenom", "date_naissance"]


# ex1 = {"identifiant": "CCCC", "nom": "Marin", "prenom": "Julie", "date_naissance": "12/08/2007"}
# ex2 = {"identifiant": "EEEE", "nom": "Renault", "prenom": "Megane", "date_naissance": "07/09/2002"}
# to_modify = ["CCCC", {"nom": "Marin", "prenom": "Julie", "date_naissance": "12/04/2011"}]
# instance_modele = JoueurModel(filter_name="identifiant", database_name=db_joueurs)

# instance_modele.enregistrer(ex1)
# instance_modele.enregistrer(ex2)
# instance_modele.supprimer(filter_value="EEEE")
# instance_modele.modifier(data_dict=to_modify[1], id_value=to_modify[0])
# check = instance_modele.entry_already_exists("AAAA")
# print(check)
# print(instance_modele.enregistrer(ex2))