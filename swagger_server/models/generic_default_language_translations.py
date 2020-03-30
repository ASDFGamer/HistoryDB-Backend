# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.language import Language  # noqa: F401,E501
from swagger_server import util


class GenericDefaultLanguageTranslations(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, language: Language=None, name: str=None):  # noqa: E501
        """GenericDefaultLanguageTranslations - a model defined in Swagger

        :param language: The language of this GenericDefaultLanguageTranslations.  # noqa: E501
        :type language: Language
        :param name: The name of this GenericDefaultLanguageTranslations.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'language': Language,
            'name': str
        }

        self.attribute_map = {
            'language': 'language',
            'name': 'name'
        }
        self._language = language
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'GenericDefaultLanguageTranslations':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GenericDefaultLanguage_translations of this GenericDefaultLanguageTranslations.  # noqa: E501
        :rtype: GenericDefaultLanguageTranslations
        """
        return util.deserialize_model(dikt, cls)

    @property
    def language(self) -> Language:
        """Gets the language of this GenericDefaultLanguageTranslations.


        :return: The language of this GenericDefaultLanguageTranslations.
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language: Language):
        """Sets the language of this GenericDefaultLanguageTranslations.


        :param language: The language of this GenericDefaultLanguageTranslations.
        :type language: Language
        """

        self._language = language

    @property
    def name(self) -> str:
        """Gets the name of this GenericDefaultLanguageTranslations.


        :return: The name of this GenericDefaultLanguageTranslations.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this GenericDefaultLanguageTranslations.


        :param name: The name of this GenericDefaultLanguageTranslations.
        :type name: str
        """

        self._name = name