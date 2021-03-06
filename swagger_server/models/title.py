# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.generic_default_language import GenericDefaultLanguage  # noqa: F401,E501
from swagger_server import util


class Title(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: GenericDefaultLanguage=None):  # noqa: E501
        """Title - a model defined in Swagger

        :param id: The id of this Title.  # noqa: E501
        :type id: int
        :param name: The name of this Title.  # noqa: E501
        :type name: GenericDefaultLanguage
        """
        self.swagger_types = {
            'id': int,
            'name': GenericDefaultLanguage
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Title':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Title of this Title.  # noqa: E501
        :rtype: Title
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Title.


        :return: The id of this Title.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Title.


        :param id: The id of this Title.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> GenericDefaultLanguage:
        """Gets the name of this Title.


        :return: The name of this Title.
        :rtype: GenericDefaultLanguage
        """
        return self._name

    @name.setter
    def name(self, name: GenericDefaultLanguage):
        """Sets the name of this Title.


        :param name: The name of this Title.
        :type name: GenericDefaultLanguage
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name
