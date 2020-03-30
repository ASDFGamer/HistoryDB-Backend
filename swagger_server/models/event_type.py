# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.generic_default_language import GenericDefaultLanguage  # noqa: F401,E501
from swagger_server import util


class EventType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: GenericDefaultLanguage=None, id: int=None):  # noqa: E501
        """EventType - a model defined in Swagger

        :param name: The name of this EventType.  # noqa: E501
        :type name: GenericDefaultLanguage
        :param id: The id of this EventType.  # noqa: E501
        :type id: int
        """
        self.swagger_types = {
            'name': GenericDefaultLanguage,
            'id': int
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id'
        }
        self._name = name
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'EventType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventType of this EventType.  # noqa: E501
        :rtype: EventType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> GenericDefaultLanguage:
        """Gets the name of this EventType.


        :return: The name of this EventType.
        :rtype: GenericDefaultLanguage
        """
        return self._name

    @name.setter
    def name(self, name: GenericDefaultLanguage):
        """Sets the name of this EventType.


        :param name: The name of this EventType.
        :type name: GenericDefaultLanguage
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self) -> int:
        """Gets the id of this EventType.


        :return: The id of this EventType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this EventType.


        :param id: The id of this EventType.
        :type id: int
        """

        self._id = id