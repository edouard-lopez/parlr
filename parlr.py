from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


class LexicalUnit(object):
    def __init__(self, name):
        self.definitions = []
        self.name = name

    def add_definition(self, definition):
        self.definitions.append(definition)

    def get_definitions(self, word):
        for definition in self.definitions:
            if word in definition:
                return [definition]


class Dictionary(object):
    def __init__(self):
        self.lexical_units = []

    def add_lexical_unit(self, lexical_unit):
        self.lexical_units.append(lexical_unit)


class Learner(object):
    def __init__(self):
        self.level = 0
        self.known_characters = []

    def learn(self, lexical_unit):
        self.known_characters.append(lexical_unit)

    def forget(self, lexical_unit):
        lexical_unit_index = self.known_characters.index(lexical_unit)
        del self.known_characters[lexical_unit_index]