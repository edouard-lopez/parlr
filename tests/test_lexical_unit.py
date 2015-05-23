# -*- coding: utf-8 -*-
import logging
from parlr import LexicalUnit

import server
import json
import unittest

logger = logging.getLogger(__name__)


class LexicalUnitTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

        root = logging.getLogger()
        root.setLevel(logging.CRITICAL)

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

    def test_create_lexical_unit_respond_201_created(self):
        response = self.app.post(
            '/lexical-units',
            data=json.dumps({'name': 'pā', 'definition': ['toucher', 'être connecté']}),
            content_type='application/json')

        self.assertEqual(201, response.status_code)

    def test_create_bad_lexical_unit_respond_400_bad_request(self):
        response = self.app.post(
            '/lexical-units',
            data=json.dumps({'name': 'pā', 'definition': ['toucher', 'être connecté']}),
            content_type='application/json')

        self.assertEqual(400, response.status_code)

    def test_return_id_of_lexical_unit(self):
        lexical_unit_id = 1
        response = self.app.post(
            '/lexical-units',
            data=json.dumps({'name': 'pā', 'definition': ['toucher', 'être connecté']}),
            content_type='application/json')
        location = '/lexical-units/' + str(lexical_unit_id)

        self.assertTrue(location in response.headers['Location'])

    def test_get_lexical_unit(self):
        response = self.app.get('/lexical-units/1', content_type='application/json')

        self.assertEqual(200, response.status_code)

    def test_get_lexical_unit_respond_404_not_found(self):
        response = self.app.get('/lexical-units/1', content_type='application/json')

        self.assertEqual(404, response.status_code)

    def test_update_lexical_unit_respond_200_ok(self):
        response = self.app.put('/lexical-units/1',
                                data=json.dumps({'name': 'pā', 'definition': ['toucher', 'être connecté']}),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)
