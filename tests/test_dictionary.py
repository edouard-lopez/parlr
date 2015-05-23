# -*- coding: utf-8 -*-
import logging
from parlr import Dictionary, LexicalUnit

import server
import json
import unittest

logger = logging.getLogger(__name__)


class DictionaryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

        root = logging.getLogger()
        root.setLevel(logging.CRITICAL)

    def test_dictionary_has_lexical_units(self):
        dictionary = Dictionary()

        self.assertEqual([], dictionary.lexical_units)

    def test_can_add_lexical_unit(self):
        dictionary = Dictionary()
        lexical_unit = LexicalUnit('pā')
        dictionary.add_lexical_unit(lexical_unit)

        self.assertEqual([lexical_unit], dictionary.lexical_units)

    def test_create_dictionary_respond_201_created(self):
        response = self.app.post(
            '/dictionaries',
            data=json.dumps({'source': 'fr', 'target': 'cn'}),
            content_type='application/json')

        self.assertEqual(201, response.status_code)

    def test_create_bad_dictionary_respond_400_bad_request(self):
        response = self.app.post(
            '/dictionaries',
            data=json.dumps({'source': '', 'target': ''}),
            content_type='application/json')

        self.assertEqual(400, response.status_code)

    def test_return_id_of_dictionary(self):
        dictionary_id = 'fr|cn'
        response = self.app.post(
            '/dictionaries',
            data=json.dumps({'source': 'fr', 'target': 'cn'}),
            content_type='application/json')
        location = '/dictionaries/' + str(dictionary_id)

        self.assertTrue(location in response.headers['Location'])

    def test_get_dictionary(self):
        response = self.app.get('/dictionaries/fr|cn', content_type='application/json')

        self.assertEqual(200, response.status_code)

    def test_get_dictionary_respond_404_not_found(self):
        response = self.app.get('/dictionaries/fr|cn', content_type='application/json')

        self.assertEqual(404, response.status_code)

    def test_update_dictionary_respond_200_ok(self):
        response = self.app.put('/dictionaries/fr|cn',
                                data=json.dumps({'source': 'fr', 'target': 'cn'}),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)
