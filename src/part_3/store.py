from category import Category

class Store:
    # attributes: name, categories (departments)
    # constructor function __init__
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    # transfers instance of a store into a string, makes debugging easier
    def __str__(self):
        output = f"Welcome to {self.name}!"

        i = 1
        # this shows the compositional relationship between Store and Category
        for category in self.categories:
            output += f'\n {i}. {category}'
            i +=1

        return output

    def __repr__(self):
        # also returns a string
        return (f'self.name = {self.name}, self.categories = {self.categories}')


