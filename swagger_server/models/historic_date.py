# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HistoricDate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, year: int=None, month: int=None, day: int=None, inaccuracy_year: int=None, inaccuracy_month: int=None, inaccuracy_day: int=None):  # noqa: E501
        """HistoricDate - a model defined in Swagger

        :param year: The year of this HistoricDate.  # noqa: E501
        :type year: int
        :param month: The month of this HistoricDate.  # noqa: E501
        :type month: int
        :param day: The day of this HistoricDate.  # noqa: E501
        :type day: int
        :param inaccuracy_year: The inaccuracy_year of this HistoricDate.  # noqa: E501
        :type inaccuracy_year: int
        :param inaccuracy_month: The inaccuracy_month of this HistoricDate.  # noqa: E501
        :type inaccuracy_month: int
        :param inaccuracy_day: The inaccuracy_day of this HistoricDate.  # noqa: E501
        :type inaccuracy_day: int
        """
        self.swagger_types = {
            'year': int,
            'month': int,
            'day': int,
            'inaccuracy_year': int,
            'inaccuracy_month': int,
            'inaccuracy_day': int
        }

        self.attribute_map = {
            'year': 'year',
            'month': 'month',
            'day': 'day',
            'inaccuracy_year': 'inaccuracy_year',
            'inaccuracy_month': 'inaccuracy_month',
            'inaccuracy_day': 'inaccuracy_day'
        }
        self._year = year
        self._month = month
        self._day = day
        self._inaccuracy_year = inaccuracy_year
        self._inaccuracy_month = inaccuracy_month
        self._inaccuracy_day = inaccuracy_day

    @classmethod
    def from_dict(cls, dikt) -> 'HistoricDate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HistoricDate of this HistoricDate.  # noqa: E501
        :rtype: HistoricDate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def year(self) -> int:
        """Gets the year of this HistoricDate.


        :return: The year of this HistoricDate.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year: int):
        """Sets the year of this HistoricDate.


        :param year: The year of this HistoricDate.
        :type year: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def month(self) -> int:
        """Gets the month of this HistoricDate.


        :return: The month of this HistoricDate.
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month: int):
        """Sets the month of this HistoricDate.


        :param month: The month of this HistoricDate.
        :type month: int
        """

        self._month = month

    @property
    def day(self) -> int:
        """Gets the day of this HistoricDate.


        :return: The day of this HistoricDate.
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day: int):
        """Sets the day of this HistoricDate.


        :param day: The day of this HistoricDate.
        :type day: int
        """

        self._day = day

    @property
    def inaccuracy_year(self) -> int:
        """Gets the inaccuracy_year of this HistoricDate.


        :return: The inaccuracy_year of this HistoricDate.
        :rtype: int
        """
        return self._inaccuracy_year

    @inaccuracy_year.setter
    def inaccuracy_year(self, inaccuracy_year: int):
        """Sets the inaccuracy_year of this HistoricDate.


        :param inaccuracy_year: The inaccuracy_year of this HistoricDate.
        :type inaccuracy_year: int
        """

        self._inaccuracy_year = inaccuracy_year

    @property
    def inaccuracy_month(self) -> int:
        """Gets the inaccuracy_month of this HistoricDate.


        :return: The inaccuracy_month of this HistoricDate.
        :rtype: int
        """
        return self._inaccuracy_month

    @inaccuracy_month.setter
    def inaccuracy_month(self, inaccuracy_month: int):
        """Sets the inaccuracy_month of this HistoricDate.


        :param inaccuracy_month: The inaccuracy_month of this HistoricDate.
        :type inaccuracy_month: int
        """

        self._inaccuracy_month = inaccuracy_month

    @property
    def inaccuracy_day(self) -> int:
        """Gets the inaccuracy_day of this HistoricDate.


        :return: The inaccuracy_day of this HistoricDate.
        :rtype: int
        """
        return self._inaccuracy_day

    @inaccuracy_day.setter
    def inaccuracy_day(self, inaccuracy_day: int):
        """Sets the inaccuracy_day of this HistoricDate.


        :param inaccuracy_day: The inaccuracy_day of this HistoricDate.
        :type inaccuracy_day: int
        """

        self._inaccuracy_day = inaccuracy_day