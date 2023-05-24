from tinydb import Query

query = Query()


class BaseManager:
    def __init__(self, modele_objet, vue_objet) -> None:
        self.instance_modele = modele_objet
        self.instance_vue = vue_objet
        self.option_choisie = ""

    def get_option(self):
        self.option_choisie = self.instance_vue.choix_option()
        return self.option_choisie

    def execution(self):
        self.get_option()

        if self.option_choisie == "ajouter":
            self.ajouter()
        elif self.option_choisie == "modifier":
            self.modifier()
        elif self.option_choisie == "supprimer":
            self.supprimer()

    def ajouter(self):
        # data = self.instance_vue.get_input_data("ajouter")
        data = self.instance_vue.ajouter()
        self.instance_modele.enregistrer_db(data)

    def modifier(self):
        id = self.instance_vue.get_id("modifier")
        new_data = self.instance_vue.get_input_data("modifier")
        self.instance_modele.modifier_db(id_value=id, data_dict=new_data)

    def supprimer(self):
        id = self.instance_vue.get_id("supprimer")
        self.instance_modele.supprimer_db(id_value=id)
