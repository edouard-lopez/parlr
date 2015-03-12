import unittest


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


class LexicalUnitTestCase(unittest.TestCase):
    def test_lexical_unit_has_definitions(self):
        name = 'pakeha'
        lexical_unit = LexicalUnit(name)

        self.assertEqual(name, lexical_unit.name)
        self.assertEqual([], lexical_unit.definitions)

    def test_lexical_unit_can_have_several_definitions(self):
        lexical_unit = LexicalUnit('pā')
        lexical_unit.add_definition('toucher')
        lexical_unit.add_definition('être connecté')
        self.assertEqual(2, len(lexical_unit.definitions))


class Dictionary(object):
    def __init__(self):
        self.lexical_units = []

    def add_lexical_unit(self, lexical_unit):
        self.lexical_units.append(lexical_unit)


class DictionaryTestCase(unittest.TestCase):
    def test_dictionary_has_lexical_units(self):
        dictionary = Dictionary()
        
        self.assertEqual([], dictionary.lexical_units)

    def test_can_add_lexical_unit(self):
        dictionary = Dictionary()
        lexical_unit = LexicalUnit('pā')
        dictionary.add_lexical_unit(lexical_unit)

        self.assertEqual([lexical_unit], dictionary.lexical_units)

if __name__ == '__main__':
    unittest.main()
