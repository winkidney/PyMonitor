#!/usr/bin/env python
# coding:utf-8
# base - 
# author : winkidney - 14-9-15
__author__ = 'winkidney'

import json


class InfoBase(object):
    """
    Base class of data getter.
    __init__ and get_asdict method must be overwrite.
    """
    def __init__(self):
        raise NotImplementedError('This base class can not be instanced directly!')

    def get_asdict(self):
        """
        :return: dict.
        """
        raise NotImplementedError('You must overwrite this method')

    def get_aslist(self):
        """

        :return: python list of (key, value).
        """
        res_dict = self.get_asdict()
        if not isinstance(res_dict, dict):
            raise TypeError('get_asdict method must return a python dict.')
        res_list = []
        for item in res_dict.items():
            res_list.append(item)
        return sorted(res_list)

    def get_asjson(self):
        """
        :return: jsons trings encoded by utf-8.
        """
        res_dict = self.get_asdict()
        if not isinstance(res_dict, dict):
            raise TypeError('get_asdict method must return a python dict.')
        return json.dumps(res_dict)

    def _format_number(self, byte_str, unit):
        """

        :param byte_str: the src number in unit `byte`
        :type byte_str: str
        :type unit: str
        :param unit: string stands for unit, `byte` or 'kb'
        :return: integer
        """
        unit = unit.upper()
        if unit not in ('BYTE', 'KB'):
            raise ValueError('Unexcepted unit parament!')
        if unit == 'KB':
            divisor = 1024
        else:
            divisor = 1
        if isinstance(byte_str, (str, unicode)) and byte_str.isdigit():
            result = int(byte_str) / divisor
        return result