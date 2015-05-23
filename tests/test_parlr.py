import unittest

from parlr import LexicalUnit, Dictionary, Learner


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


class DictionaryTestCase(unittest.TestCase):
    def test_dictionary_has_lexical_units(self):
        dictionary = Dictionary()
        
        self.assertEqual([], dictionary.lexical_units)

    def test_can_add_lexical_unit(self):
        dictionary = Dictionary()
        lexical_unit = LexicalUnit('pā')
        dictionary.add_lexical_unit(lexical_unit)

        self.assertEqual([lexical_unit], dictionary.lexical_units)


class LearnerTestCase(unittest.TestCase):
    def test_learner_knows_a_list_of_characters(self):
        learner = Learner()

        self.assertEqual([], learner.known_characters)

    def test_learner_can_learn_lexical_unit(self):
        learner = Learner()

        lexical_unit = 'pakeha'
        learner.learn(lexical_unit)

        self.assertEqual([lexical_unit], learner.known_characters)

    def test_learner_can_forget_a_lexical_unit(self):
        learner = Learner()

        lexical_unit = 'pakeha'
        learner.learn(lexical_unit)
        learner.forget(lexical_unit)

        self.assertEqual([], learner.known_characters)

    def test_learner_has_a_linguistic_level(self):
        # arrange
        learner = Learner()

        # act

        # assert
        self.assertEqual(0, learner.level)



if __name__ == '__main__':
    unittest.main()
