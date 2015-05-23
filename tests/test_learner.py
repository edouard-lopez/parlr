# -*- coding: utf-8 -*-
import logging
from parlr import Learner

import server
import json
import unittest

logger = logging.getLogger(__name__)


class LearnerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

        root = logging.getLogger()
        root.setLevel(logging.CRITICAL)

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

    def test_create_learner_respond_201_created(self):
        response = self.app.post(
            '/learners',
            data=json.dumps({'username': 'Édouard Lopez', 'level': 0, 'known_characters': []}),
            content_type='application/json')

        self.assertEqual(201, response.status_code)

    def test_create_bad_learner_respond_400_bad_request(self):
        response = self.app.post(
            '/learners',
            data=json.dumps({'username': '', 'level': 0, 'known_characters': []}),
            content_type='application/json')

        self.assertEqual(400, response.status_code)

    def test_return_id_of_learner(self):
        learner_id = 1
        response = self.app.post(
            '/learners',
            data=json.dumps({'username': 'Édouard Lopez', 'level': 0, 'known_characters': []}),
            content_type='application/json')
        location = '/learners/' + str(learner_id)

        self.assertTrue(location in response.headers['Location'])

    def test_get_learner(self):
        response = self.app.get('/learners/1', content_type='application/json')

        self.assertEqual(200, response.status_code)

    def test_get_learner_respond_404_not_found(self):
        response = self.app.get('/learners/1', content_type='application/json')

        self.assertEqual(404, response.status_code)

    def test_update_learner_respond_200_ok(self):
        response = self.app.put('/learners/1',
                                data=json.dumps({'username': 'Édouard Lopez', 'level': 1, 'known_characters': [1,2]}),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)
