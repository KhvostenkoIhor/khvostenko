class Restaurant():
    """Простое описание ресторана"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def descript(self):
        print("Ресторан " + self.name.title() + " приветствует тебя")
        print("В меню преобладает " + self.cuisine + " кухня")
    def open_rest(self):
        print("Милости просим. Мы открыты")
    def closed_rest(self):
        print("К сожалению, " + self.name.title() + " закрыт. Приходи завтра")

my_rest = Restaurant("Gogol", "Europian")

my_rest.descript()
my_rest.open_rest()
my_rest.closed_rest()