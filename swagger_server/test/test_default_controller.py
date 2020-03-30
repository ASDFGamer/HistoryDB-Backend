# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.border import Border  # noqa: E501
from swagger_server.models.country import Country  # noqa: E501
from swagger_server.models.country_relation import CountryRelation  # noqa: E501
from swagger_server.models.event import Event  # noqa: E501
from swagger_server.models.event_relation import EventRelation  # noqa: E501
from swagger_server.models.event_type import EventType  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response409 import InlineResponse409  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.person_relation import PersonRelation  # noqa: E501
from swagger_server.models.relation_type import RelationType  # noqa: E501
from swagger_server.models.settlement_relation import SettlementRelation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_operations_country_create_border(self):
        """Test case for operations_country_create_border

        
        """
        body = Border()
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/border'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_create_country(self):
        """Test case for operations_country_create_country

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_create_country_relation(self):
        """Test case for operations_country_create_country_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/country'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_create_event_relation(self):
        """Test case for operations_country_create_event_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/event'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_create_person_relation(self):
        """Test case for operations_country_create_person_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/person'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_create_settlement_relation(self):
        """Test case for operations_country_create_settlement_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/settlement'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_delete_border(self):
        """Test case for operations_country_delete_border

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/border/{year}'.format(year=56, id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_delete_country(self):
        """Test case for operations_country_delete_country

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_delete_country_relation(self):
        """Test case for operations_country_delete_country_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/country/{country_id}'.format(id=789, country_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_delete_event_relation(self):
        """Test case for operations_country_delete_event_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/event/{event_id}'.format(id=789, event_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_delete_person_relation(self):
        """Test case for operations_country_delete_person_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/person/{person_id}'.format(id=789, person_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_delete_settlement_relation(self):
        """Test case for operations_country_delete_settlement_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/settlement/{settlement_id}'.format(id=789, settlement_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_get_border(self):
        """Test case for operations_country_get_border

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/border/{year}'.format(year=56, id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_get_country(self):
        """Test case for operations_country_get_country

        
        """
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}'.format(id=789),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_list_borders(self):
        """Test case for operations_country_list_borders

        
        """
        query_string = [('limit', 56),
                        ('offset', 56),
                        ('year', 56)]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/borders'.format(id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_list_countries(self):
        """Test case for operations_country_list_countries

        
        """
        query_string = [('limit', 56),
                        ('offset', 56),
                        ('year', 56),
                        ('population', 2)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/countries',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_list_country_relations(self):
        """Test case for operations_country_list_country_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/countries'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_list_event_relations(self):
        """Test case for operations_country_list_event_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/events'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_list_person_relations(self):
        """Test case for operations_country_list_person_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/persons'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_list_settlement_relations(self):
        """Test case for operations_country_list_settlement_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/settlements'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_update_border(self):
        """Test case for operations_country_update_border

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}/border/{year}'.format(year=56, id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_country_update_country(self):
        """Test case for operations_country_update_country

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/country/{id}'.format(id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_create_country_relation(self):
        """Test case for operations_event_create_country_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/country'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_create_event(self):
        """Test case for operations_event_create_event

        
        """
        body = Event()
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_create_event_relation(self):
        """Test case for operations_event_create_event_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/event'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_create_person_relation(self):
        """Test case for operations_event_create_person_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/person'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_create_settlement_relation(self):
        """Test case for operations_event_create_settlement_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/settlement'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_delete_country_relation(self):
        """Test case for operations_event_delete_country_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/country/{country_id}'.format(id=789, country_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_delete_event(self):
        """Test case for operations_event_delete_event

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_delete_event_relation(self):
        """Test case for operations_event_delete_event_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/event/{event_id}'.format(id=789, event_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_delete_person_relation(self):
        """Test case for operations_event_delete_person_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/person/{person_id}'.format(id=789, person_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_delete_settlement_relation(self):
        """Test case for operations_event_delete_settlement_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/settlement/{settlement_id}'.format(id=789, settlement_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_get_event(self):
        """Test case for operations_event_get_event

        
        """
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}'.format(id=789),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_list_country_relations(self):
        """Test case for operations_event_list_country_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/countries'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_list_event_relations(self):
        """Test case for operations_event_list_event_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/events'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_list_events(self):
        """Test case for operations_event_list_events

        
        """
        query_string = [('limit', 56),
                        ('offset', 56),
                        ('year', 56),
                        ('month', 12),
                        ('day', 31)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/events',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_list_person_relations(self):
        """Test case for operations_event_list_person_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/persons'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_list_settlement_relations(self):
        """Test case for operations_event_list_settlement_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}/settlements'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_event_update_event(self):
        """Test case for operations_event_update_event

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/event/{id}'.format(id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_create_country_relation(self):
        """Test case for operations_person_create_country_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/country'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_create_event_relation(self):
        """Test case for operations_person_create_event_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/event'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_create_person(self):
        """Test case for operations_person_create_person

        
        """
        body = Person()
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_create_person_relation(self):
        """Test case for operations_person_create_person_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/person'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_create_settlement_relation(self):
        """Test case for operations_person_create_settlement_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/settlement'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_delete_country_relation(self):
        """Test case for operations_person_delete_country_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/country/{country_id}'.format(id=789, country_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_delete_event_relation(self):
        """Test case for operations_person_delete_event_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/event/{event_id}'.format(id=789, event_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_delete_person(self):
        """Test case for operations_person_delete_person

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_delete_person_relation(self):
        """Test case for operations_person_delete_person_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/person/{person_id}'.format(id=789, person_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_delete_settlement_relation(self):
        """Test case for operations_person_delete_settlement_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/settlement/{settlement_id}'.format(id=789, settlement_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_get_person(self):
        """Test case for operations_person_get_person

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_list_country_relations(self):
        """Test case for operations_person_list_country_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/countries'.format(id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_list_event_relations(self):
        """Test case for operations_person_list_event_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/events'.format(id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_list_person_relations(self):
        """Test case for operations_person_list_person_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/persons'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_list_persons(self):
        """Test case for operations_person_list_persons

        
        """
        query_string = [('limit', 56),
                        ('offset', 56),
                        ('year', 56)]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/persons',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_list_settlement_relations(self):
        """Test case for operations_person_list_settlement_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}/settlements'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_person_update_person(self):
        """Test case for operations_person_update_person

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/person/{id}'.format(id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_create_country_relation(self):
        """Test case for operations_settlement_create_country_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/country'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_create_event_relation(self):
        """Test case for operations_settlement_create_event_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/event'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_create_person_relation(self):
        """Test case for operations_settlement_create_person_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/person'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_create_settlement(self):
        """Test case for operations_settlement_create_settlement

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_create_settlement_relation(self):
        """Test case for operations_settlement_create_settlement_relation

        
        """
        body = None
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/settlement'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_delete_country_relation(self):
        """Test case for operations_settlement_delete_country_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/country/{country_id}'.format(id=789, country_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_delete_event_relation(self):
        """Test case for operations_settlement_delete_event_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/event/{event_id}'.format(id=789, event_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_delete_person_relation(self):
        """Test case for operations_settlement_delete_person_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/person/{person_id}'.format(id=789, person_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_delete_settlement(self):
        """Test case for operations_settlement_delete_settlement

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_delete_settlement_relation(self):
        """Test case for operations_settlement_delete_settlement_relation

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/settlement/{settlement_id}'.format(id=789, settlement_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_get_settlement(self):
        """Test case for operations_settlement_get_settlement

        
        """
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}'.format(id=789),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_list_country_relations(self):
        """Test case for operations_settlement_list_country_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/countries'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_list_event_relations(self):
        """Test case for operations_settlement_list_event_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/events'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_list_person_relations(self):
        """Test case for operations_settlement_list_person_relations

        
        """
        query_string = [('type', 789),
                        ('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/persons'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_list_settlement_relations(self):
        """Test case for operations_settlement_list_settlement_relations

        
        """
        query_string = [('limit', 56),
                        ('offset', 56),
                        ('type', 789)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}/settlements'.format(id=789),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_list_settlements(self):
        """Test case for operations_settlement_list_settlements

        
        """
        query_string = [('limit', 56),
                        ('offset', 56),
                        ('year', 56),
                        ('population', 2)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlements',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_settlement_update_settlement(self):
        """Test case for operations_settlement_update_settlement

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/settlement/{id}'.format(id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_add_event_type(self):
        """Test case for operations_types_add_event_type

        adds an eventtype
        """
        body = EventType()
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/event',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_add_relation_type(self):
        """Test case for operations_types_add_relation_type

        adds an relationtype
        """
        body = EventType()
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/relation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_delete_event_type(self):
        """Test case for operations_types_delete_event_type

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/event/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_delete_relation_type(self):
        """Test case for operations_types_delete_relation_type

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/relation/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_get_event_type(self):
        """Test case for operations_types_get_event_type

        
        """
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/event/{id}'.format(id=789),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_get_relation_type(self):
        """Test case for operations_types_get_relation_type

        
        """
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/relation/{id}'.format(id=789),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_list_event_types(self):
        """Test case for operations_types_list_event_types

        
        """
        query_string = [('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/events',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_list_relation_types(self):
        """Test case for operations_types_list_relation_types

        
        """
        query_string = [('limit', 56),
                        ('offset', 56)]
        headers = [('accept_language', 'accept_language_example')]
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/relations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_update_event_type(self):
        """Test case for operations_types_update_event_type

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/event/{id}'.format(id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_types_update_relation_type(self):
        """Test case for operations_types_update_relation_type

        
        """
        response = self.client.open(
            '/ASDFOrg/HistoryDB/1.0.0/type/relation/{id}'.format(id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
