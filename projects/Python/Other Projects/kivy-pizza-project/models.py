
class Pizza():
    name = ""
    ingredients = ""
    price = 0.0
    vegetarian = False
    spicy = False

    def __init__(self, name, ingredients, price, vegetarian, spicy):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.vegetarian = vegetarian
        self.spicy = spicy

    def get_dictionary(self):
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "price": self.price,
            "vegetarian": self.vegetarian,
            "spicy": self.spicy,
        }
