from tinydb import Query

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

    def enregistrer_db(self, new_entry):
        if not self.entry_already_exists(new_entry[self.default_filter]):
            self.database.insert(new_entry)
            return new_entry
        else:
            return "Cette entrée existe déjà dans la base de données"

    def modifier_db(self, data_dict, id_value):
        self.database.update(data_dict, query[self.default_filter] == id_value)

    def supprimer_db(self, id_value):
        self.database.remove(query[self.default_filter] == id_value)

    def retreive_all_db(self):
        print(self.database.all())

    def retreive_entry_db(self, filter_value):
        entry = self.database.search(query[self.default_filter] == filter_value)
        return entry
