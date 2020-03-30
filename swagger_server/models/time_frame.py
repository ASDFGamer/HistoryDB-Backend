# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.historic_date import HistoricDate  # noqa: F401,E501
from swagger_server import util


class TimeFrame(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, start: HistoricDate=None, end: HistoricDate=None):  # noqa: E501
        """TimeFrame - a model defined in Swagger

        :param start: The start of this TimeFrame.  # noqa: E501
        :type start: HistoricDate
        :param end: The end of this TimeFrame.  # noqa: E501
        :type end: HistoricDate
        """
        self.swagger_types = {
            'start': HistoricDate,
            'end': HistoricDate
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end'
        }
        self._start = start
        self._end = end

    @classmethod
    def from_dict(cls, dikt) -> 'TimeFrame':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimeFrame of this TimeFrame.  # noqa: E501
        :rtype: TimeFrame
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self) -> HistoricDate:
        """Gets the start of this TimeFrame.


        :return: The start of this TimeFrame.
        :rtype: HistoricDate
        """
        return self._start

    @start.setter
    def start(self, start: HistoricDate):
        """Sets the start of this TimeFrame.


        :param start: The start of this TimeFrame.
        :type start: HistoricDate
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self) -> HistoricDate:
        """Gets the end of this TimeFrame.


        :return: The end of this TimeFrame.
        :rtype: HistoricDate
        """
        return self._end

    @end.setter
    def end(self, end: HistoricDate):
        """Sets the end of this TimeFrame.


        :param end: The end of this TimeFrame.
        :type end: HistoricDate
        """

        self._end = end
