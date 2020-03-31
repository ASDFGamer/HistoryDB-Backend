import connexion
import six

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
from swagger_server import util


def operations_country_create_border(id, body=None):  # noqa: E501
    """operations_country_create_border

    Creates a new border # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: Border
    """
    if connexion.request.is_json:
        body = Border.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.country.createborder(id, body)


def operations_country_create_country():  # noqa: E501
    """operations_country_create_country

    Creates an new Country # noqa: E501


    :rtype: Country
    """
    return swagger_server.services.country.createcountry()


def operations_country_create_country_relation(id, body=None):  # noqa: E501
    """operations_country_create_country_relation

    Link an existing country to this country # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.country.createcountryrelation(id, body)


def operations_country_create_event_relation(id, body=None):  # noqa: E501
    """operations_country_create_event_relation

    Link an existing event to this country # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.country.createeventrelation(id, body)


def operations_country_create_person_relation(id, body=None):  # noqa: E501
    """operations_country_create_person_relation

    Link an existing person to this country # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.country.createpersonrelation(id, body)


def operations_country_create_settlement_relation(id, body=None):  # noqa: E501
    """operations_country_create_settlement_relation

    Link an existing settlement to this country # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.country.createsettlementrelation(id, body)


def operations_country_delete_border(year, id):  # noqa: E501
    """operations_country_delete_border

    Deletes the info about border of the country # noqa: E501

    :param year: Specifies the year of the results
    :type year: int
    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.country.deleteborder(year, id)


def operations_country_delete_country(id):  # noqa: E501
    """operations_country_delete_country

    Deletes an specific country # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.country.deletecountry(id)


def operations_country_delete_country_relation(id, country_id):  # noqa: E501
    """operations_country_delete_country_relation

    Deletes the Link between the country and the country # noqa: E501

    :param id: 
    :type id: int
    :param country_id: 
    :type country_id: int

    :rtype: None
    """
    return swagger_server.services.country.deletecountryrelation(id, country_id)


def operations_country_delete_event_relation(id, event_id):  # noqa: E501
    """operations_country_delete_event_relation

    Deletes the Link between the country and the event # noqa: E501

    :param id: 
    :type id: int
    :param event_id: 
    :type event_id: int

    :rtype: None
    """
    return swagger_server.services.country.deleteeventrelation(id, event_id)


def operations_country_delete_person_relation(id, person_id):  # noqa: E501
    """operations_country_delete_person_relation

    Deletes the Link between the country and the person # noqa: E501

    :param id: 
    :type id: int
    :param person_id: 
    :type person_id: int

    :rtype: None
    """
    return swagger_server.services.country.deletepersonrelation(id, person_id)


def operations_country_delete_settlement_relation(id, settlement_id):  # noqa: E501
    """operations_country_delete_settlement_relation

    Deletes the Link between the country and the settlement # noqa: E501

    :param id: 
    :type id: int
    :param settlement_id: 
    :type settlement_id: int

    :rtype: None
    """
    return swagger_server.services.country.deletesettlementrelation(id, settlement_id)


def operations_country_get_border(year, id):  # noqa: E501
    """operations_country_get_border

     # noqa: E501

    :param year: Specifies the year of the results
    :type year: int
    :param id: 
    :type id: int

    :rtype: Border
    """
    return swagger_server.services.country.getborder(year, id)


def operations_country_get_country(id, accept_language=None):  # noqa: E501
    """operations_country_get_country

    Returns an specific country # noqa: E501

    :param id: 
    :type id: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: Country
    """
    return swagger_server.services.country.getcountry(id, accept_language)


def operations_country_list_borders(id, limit=None, offset=None, year=None):  # noqa: E501
    """operations_country_list_borders

    A List of all known Borders for the country # noqa: E501

    :param id: 
    :type id: int
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param year: Specifies the year of the results
    :type year: int

    :rtype: List[Border]
    """
    return swagger_server.services.country.listborders(id, limit, offset, year)


def operations_country_list_countries(limit=None, offset=None, year=None, population=None, accept_language=None):  # noqa: E501
    """operations_country_list_countries

    Returns an List of all Countries # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param year: Specifies the year of the results
    :type year: int
    :param population: Specifies the minimal polulation
    :type population: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: List[Country]
    """
    return swagger_server.services.country.listcountries(limit, offset, year, population, accept_language)


def operations_country_list_country_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_country_list_country_relations

    A List with all countrys that are related to the country # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[CountryRelation]
    """
    return swagger_server.services.country.listcountryrelations(id, type, accept_language, limit, offset)


def operations_country_list_event_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_country_list_event_relations

    A List with all events that are related to the country # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[EventRelation]
    """
    return swagger_server.services.country.listeventrelations(id, type, accept_language, limit, offset)


def operations_country_list_person_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_country_list_person_relations

    A List with all country that are related to the person # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[PersonRelation]
    """
    return swagger_server.services.country.listpersonrelations(id, type, accept_language, limit, offset)


def operations_country_list_settlement_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_country_list_settlement_relations

    A List with all settlements that are related to the country # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[SettlementRelation]
    """
    return swagger_server.services.country.listsettlementrelations(id, type, accept_language, limit, offset)


def operations_country_update_border(year, id):  # noqa: E501
    """operations_country_update_border

    Updates the info about the country border for that year # noqa: E501

    :param year: Specifies the year of the results
    :type year: int
    :param id: 
    :type id: int

    :rtype: Border
    """
    return swagger_server.services.country.updateborder(year, id)


def operations_country_update_country(id):  # noqa: E501
    """operations_country_update_country

    Updates an specific country # noqa: E501

    :param id: 
    :type id: int

    :rtype: Country
    """
    return swagger_server.services.country.updatecountry(id)


def operations_event_create_country_relation(id, body=None):  # noqa: E501
    """operations_event_create_country_relation

    Link an existing country to this event # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.event.createcountryrelation(id, body)


def operations_event_create_event(body=None):  # noqa: E501
    """operations_event_create_event

    Creates an new event # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.event.createevent(body)


def operations_event_create_event_relation(id, body=None):  # noqa: E501
    """operations_event_create_event_relation

    Link an existing event to this event # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.event.createeventrelation(id, body)


def operations_event_create_person_relation(id, body=None):  # noqa: E501
    """operations_event_create_person_relation

    Link an existing person to this event # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.event.createpersonrelation(id, body)


def operations_event_create_settlement_relation(id, body=None):  # noqa: E501
    """operations_event_create_settlement_relation

    Link an existing settlement to this event # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.event.createsettlementrelation(id, body)


def operations_event_delete_country_relation(id, country_id):  # noqa: E501
    """operations_event_delete_country_relation

    Deletes the Link between the event and the country # noqa: E501

    :param id: 
    :type id: int
    :param country_id: 
    :type country_id: int

    :rtype: None
    """
    return swagger_server.services.event.deletecountryrelation(id, country_id)


def operations_event_delete_event(id):  # noqa: E501
    """operations_event_delete_event

    Deletes an specific event # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.event.deleteevent(id)


def operations_event_delete_event_relation(id, event_id):  # noqa: E501
    """operations_event_delete_event_relation

    Deletes the Link between the event and the event # noqa: E501

    :param id: 
    :type id: int
    :param event_id: 
    :type event_id: int

    :rtype: None
    """
    return swagger_server.services.event.deleteeventrelation(id, event_id)


def operations_event_delete_person_relation(id, person_id):  # noqa: E501
    """operations_event_delete_person_relation

    Deletes the Link between the event and the person # noqa: E501

    :param id: 
    :type id: int
    :param person_id: 
    :type person_id: int

    :rtype: None
    """
    return swagger_server.services.event.deletepersonrelation(id, person_id)


def operations_event_delete_settlement_relation(id, settlement_id):  # noqa: E501
    """operations_event_delete_settlement_relation

    Deletes the Link between the event and the settlement # noqa: E501

    :param id: 
    :type id: int
    :param settlement_id: 
    :type settlement_id: int

    :rtype: None
    """
    return swagger_server.services.event.deletesettlementrelation(id, settlement_id)


def operations_event_get_event(id, accept_language=None):  # noqa: E501
    """operations_event_get_event

    Returns an specific event # noqa: E501

    :param id: 
    :type id: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: Event
    """
    return swagger_server.services.event.getevent(id, accept_language)


def operations_event_list_country_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_event_list_country_relations

    A List with all countrys that are related to the event # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[CountryRelation]
    """
    return swagger_server.services.event.listcountryrelations(id, type, accept_language, limit, offset)


def operations_event_list_event_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_event_list_event_relations

    A List with all events that are related to the event # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[EventRelation]
    """
    return swagger_server.services.event.listeventrelations(id, type, accept_language, limit, offset)


def operations_event_list_events(limit=None, offset=None, year=None, month=None, day=None, accept_language=None):  # noqa: E501
    """operations_event_list_events

    Returns an list of all events # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param year: Specifies the year of the results
    :type year: int
    :param month: Specifies the month of the event
    :type month: int
    :param day: Specufies the day of the month of the event
    :type day: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: List[Event]
    """
    return swagger_server.services.event.listevents(limit, offset, year, month, day, accept_language)


def operations_event_list_person_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_event_list_person_relations

    A List with all event that are related to the person # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[PersonRelation]
    """
    return swagger_server.services.event.listpersonrelations(id, type, accept_language, limit, offset)


def operations_event_list_settlement_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_event_list_settlement_relations

    A List with all settlements that are related to the event # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[SettlementRelation]
    """
    return swagger_server.services.event.listsettlementrelations(id, type, accept_language, limit, offset)


def operations_event_update_event(id):  # noqa: E501
    """operations_event_update_event

    Updates an specific event # noqa: E501

    :param id: 
    :type id: int

    :rtype: Event
    """
    return swagger_server.services.event.updateevent(id)


def operations_person_create_country_relation(id, body=None):  # noqa: E501
    """operations_person_create_country_relation

    Link an existing country to this person # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.person.createcountryrelation(id, body)


def operations_person_create_event_relation(id, body=None):  # noqa: E501
    """operations_person_create_event_relation

    Link an existing event to this person # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.person.createeventrelation(id, body)


def operations_person_create_person(body=None):  # noqa: E501
    """operations_person_create_person

    Creates a new Person # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Person.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.person.createperson(body)


def operations_person_create_person_relation(id, body=None):  # noqa: E501
    """operations_person_create_person_relation

    Link an existing person to this person # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.person.createpersonrelation(id, body)


def operations_person_create_settlement_relation(id, body=None):  # noqa: E501
    """operations_person_create_settlement_relation

    Link an existing settlement to this person # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.person.createsettlementrelation(id, body)


def operations_person_delete_country_relation(id, country_id):  # noqa: E501
    """operations_person_delete_country_relation

    Deletes the Link between the person and the country # noqa: E501

    :param id: 
    :type id: int
    :param country_id: 
    :type country_id: int

    :rtype: None
    """
    return swagger_server.services.person.deletecountryrelation(id, country_id)


def operations_person_delete_event_relation(id, event_id):  # noqa: E501
    """operations_person_delete_event_relation

    Deletes the Link between the person and the event # noqa: E501

    :param id: 
    :type id: int
    :param event_id: 
    :type event_id: int

    :rtype: None
    """
    return swagger_server.services.person.deleteeventrelation(id, event_id)


def operations_person_delete_person(id):  # noqa: E501
    """operations_person_delete_person

    Deletes the Info for an Person # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.person.deleteperson(id)


def operations_person_delete_person_relation(id, person_id):  # noqa: E501
    """operations_person_delete_person_relation

    Deletes the Link between the person and the person # noqa: E501

    :param id: 
    :type id: int
    :param person_id: 
    :type person_id: int

    :rtype: None
    """
    return swagger_server.services.person.deletepersonrelation(id, person_id)


def operations_person_delete_settlement_relation(id, settlement_id):  # noqa: E501
    """operations_person_delete_settlement_relation

    Deletes the Link between the person and the settlement # noqa: E501

    :param id: 
    :type id: int
    :param settlement_id: 
    :type settlement_id: int

    :rtype: None
    """
    return swagger_server.services.person.deletesettlementrelation(id, settlement_id)


def operations_person_get_person(id):  # noqa: E501
    """operations_person_get_person

    Returns the person with that id # noqa: E501

    :param id: 
    :type id: int

    :rtype: Person
    """
    return swagger_server.services.person.getperson(id)


def operations_person_list_country_relations(id, type=None, limit=None, offset=None):  # noqa: E501
    """operations_person_list_country_relations

    A List with all countrys that are related to the person # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[CountryRelation]
    """
    return swagger_server.services.person.listcountryrelations(id, type, limit, offset)


def operations_person_list_event_relations(id, type=None, limit=None, offset=None):  # noqa: E501
    """operations_person_list_event_relations

    A List with all events that are related to the person # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[EventRelation]
    """
    return swagger_server.services.person.listeventrelations(id, type, limit, offset)


def operations_person_list_person_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_person_list_person_relations

    A List with all persons that are related to the person # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[PersonRelation]
    """
    return swagger_server.services.person.listpersonrelations(id, type, accept_language, limit, offset)


def operations_person_list_persons(limit=None, offset=None, year=None):  # noqa: E501
    """operations_person_list_persons

    Returns a list of all Persons # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param year: Specifies the year of the results
    :type year: int

    :rtype: None
    """
    return swagger_server.services.person.listpersons(limit, offset, year)


def operations_person_list_settlement_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_person_list_settlement_relations

    A List with all settlements that are related to the person # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[SettlementRelation]
    """
    return swagger_server.services.person.listsettlementrelations(id, type, accept_language, limit, offset)


def operations_person_update_person(id):  # noqa: E501
    """operations_person_update_person

    Updates the Info for an Person # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.person.updateperson(id)


def operations_settlement_create_country_relation(id, body=None):  # noqa: E501
    """operations_settlement_create_country_relation

    Link an existing country to this settlement # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.settlement.createcountryrelation(id, body)


def operations_settlement_create_event_relation(id, body=None):  # noqa: E501
    """operations_settlement_create_event_relation

    Link an existing event to this settlement # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.settlement.createeventrelation(id, body)


def operations_settlement_create_person_relation(id, body=None):  # noqa: E501
    """operations_settlement_create_person_relation

    Link an existing person to this settlement # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.settlement.createpersonrelation(id, body)


def operations_settlement_create_settlement():  # noqa: E501
    """operations_settlement_create_settlement

    Creates a new settlement # noqa: E501


    :rtype: None
    """
    return swagger_server.services.settlement.createsettlement()


def operations_settlement_create_settlement_relation(id, body=None):  # noqa: E501
    """operations_settlement_create_settlement_relation

    Link an existing settlement to this settlement # noqa: E501

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.settlement.createsettlementrelation(id, body)


def operations_settlement_delete_country_relation(id, country_id):  # noqa: E501
    """operations_settlement_delete_country_relation

    Deletes the Link between the settlement and the country # noqa: E501

    :param id: 
    :type id: int
    :param country_id: 
    :type country_id: int

    :rtype: None
    """
    return swagger_server.services.settlement.deletecountryrelation(id, country_id)


def operations_settlement_delete_event_relation(id, event_id):  # noqa: E501
    """operations_settlement_delete_event_relation

    Deletes the Link between the settlement and the event # noqa: E501

    :param id: 
    :type id: int
    :param event_id: 
    :type event_id: int

    :rtype: None
    """
    return swagger_server.services.settlement.deleteeventrelation(id, event_id)


def operations_settlement_delete_person_relation(id, person_id):  # noqa: E501
    """operations_settlement_delete_person_relation

    Deletes the Link between the settlement and the person # noqa: E501

    :param id: 
    :type id: int
    :param person_id: 
    :type person_id: int

    :rtype: None
    """
    return swagger_server.services.settlement.deletepersonrelation(id, person_id)


def operations_settlement_delete_settlement(id):  # noqa: E501
    """operations_settlement_delete_settlement

    Deletes the Info for an settlement # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.settlement.deletesettlement(id)


def operations_settlement_delete_settlement_relation(id, settlement_id):  # noqa: E501
    """operations_settlement_delete_settlement_relation

    Deletes the Link between the settlement and the settlement # noqa: E501

    :param id: 
    :type id: int
    :param settlement_id: 
    :type settlement_id: int

    :rtype: None
    """
    return swagger_server.services.settlement.deletesettlementrelation(id, settlement_id)


def operations_settlement_get_settlement(id, accept_language=None):  # noqa: E501
    """operations_settlement_get_settlement

    Returns the settlement with that id # noqa: E501

    :param id: 
    :type id: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: None
    """
    return swagger_server.services.settlement.getsettlement(id, accept_language)


def operations_settlement_list_country_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_settlement_list_country_relations

    A List with all countrys that are related to the settlement # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[CountryRelation]
    """
    return swagger_server.services.settlement.listcountryrelations(id, type, accept_language, limit, offset)


def operations_settlement_list_event_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_settlement_list_event_relations

    A List with all events that are related to the settlement # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[EventRelation]
    """
    return swagger_server.services.settlement.listeventrelations(id, type, accept_language, limit, offset)


def operations_settlement_list_person_relations(id, type=None, accept_language=None, limit=None, offset=None):  # noqa: E501
    """operations_settlement_list_person_relations

    A List with all persons that are related to the settlement # noqa: E501

    :param id: 
    :type id: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[PersonRelation]
    """
    return swagger_server.services.settlement.listpersonrelations(id, type, accept_language, limit, offset)


def operations_settlement_list_settlement_relations(id, limit=None, offset=None, type=None, accept_language=None):  # noqa: E501
    """operations_settlement_list_settlement_relations

    A List with all settlements that are related to the settlement # noqa: E501

    :param id: 
    :type id: int
    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param type: Specifies the relation to the event
    :type type: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: List[SettlementRelation]
    """
    return swagger_server.services.settlement.listsettlementrelations(id, limit, offset, type, accept_language)


def operations_settlement_list_settlements(limit=None, offset=None, year=None, population=None, accept_language=None):  # noqa: E501
    """operations_settlement_list_settlements

    Returns a list with all settlements # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param year: Specifies the year of the results
    :type year: int
    :param population: Specifies the minimal polulation
    :type population: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: None
    """
    return swagger_server.services.settlement.listsettlements(limit, offset, year, population, accept_language)


def operations_settlement_update_settlement(id):  # noqa: E501
    """operations_settlement_update_settlement

    Updates the Info for an Settlement # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.settlement.updatesettlement(id)


def operations_types_add_event_type(body=None):  # noqa: E501
    """adds an eventtype

     # noqa: E501

    :param body: Event type to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = EventType.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.types.addeventtype(body)


def operations_types_add_relation_type(body=None):  # noqa: E501
    """adds an relationtype

     # noqa: E501

    :param body: Relation type to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = EventType.from_dict(connexion.request.get_json())  # noqa: E501
    return swagger_server.services.types.addrelationtype(body)


def operations_types_delete_event_type(id):  # noqa: E501
    """operations_types_delete_event_type

    Deletes an specific event type # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.types.deleteeventtype(id)


def operations_types_delete_relation_type(id):  # noqa: E501
    """operations_types_delete_relation_type

    Deletes an specific relation type # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return swagger_server.services.types.deleterelationtype(id)


def operations_types_get_event_type(id, accept_language=None):  # noqa: E501
    """operations_types_get_event_type

    Returns an specific event type # noqa: E501

    :param id: 
    :type id: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: EventType
    """
    return swagger_server.services.types.geteventtype(id, accept_language)


def operations_types_get_relation_type(id, accept_language=None):  # noqa: E501
    """operations_types_get_relation_type

    Returns an specific relation type # noqa: E501

    :param id: 
    :type id: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: EventType
    """
    return swagger_server.services.types.getrelationtype(id, accept_language)


def operations_types_list_event_types(limit=None, offset=None, accept_language=None):  # noqa: E501
    """operations_types_list_event_types

    Returns all event types # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: List[EventType]
    """
    return swagger_server.services.types.listeventtypes(limit, offset, accept_language)


def operations_types_list_relation_types(limit=None, offset=None, accept_language=None):  # noqa: E501
    """operations_types_list_relation_types

    Returns all relation types # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int
    :param accept_language: Specifies the language of the result
    :type accept_language: str

    :rtype: List[RelationType]
    """
    return swagger_server.services.types.listrelationtypes(limit, offset, accept_language)


def operations_types_update_event_type(id):  # noqa: E501
    """operations_types_update_event_type

    Updates an specific event type # noqa: E501

    :param id: 
    :type id: int

    :rtype: EventType
    """
    return swagger_server.services.types.updateeventtype(id)


def operations_types_update_relation_type(id):  # noqa: E501
    """operations_types_update_relation_type

    Updates an specific event type # noqa: E501

    :param id: 
    :type id: int

    :rtype: EventType
    """
    return swagger_server.services.types.updaterelationtype(id)
