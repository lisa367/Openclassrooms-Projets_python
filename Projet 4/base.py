from tinydb import TinyDB, Query

query = Query()

class BaseModel:
    def __init__(self, filter_name, database_name):
        self.data_dict = {}
        self.default_filter = filter_name
        self.database = database_name
    
    def entry_already_exists(self, filter_value):
        id_check = self.database.search(query[self.default_filter] == filter_value)
        if id_check:
            return id_check
        else:
            return None

    def enregistrer(self, new_entry):
        if not self.entry_already_exists(new_entry[self.default_filter]):
            self.database.insert(new_entry)
            return new_entry
        else:
            return "Cette entrée existe déjà dans la base de données"

    def modifier(self, data_dict, id_value):
        self.database.update(data_dict, query[self.default_filter] == id_value)

    def supprimer(self, filter_value):
        self.database.remove(query[self.default_filter] == filter_value)

    def retreive_all(self):
        print(self.database.all())