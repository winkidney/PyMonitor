#!/usr/bin/env python
# coding:utf-8
# net - 
# author : winkidney - 14-9-16
__author__ = 'winkidney'

import logging

from .base import InfoBase


class Network(InfoBase):

    def __init__(self):
        try:
            self.network = open('/proc/net/dev', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read /proc/net/dev !")

    def get_asdict(self, unit='byte'):
        """
        only tested on by ubuntu!
        :return: a null dict if file reading failed.
        :return: a dict(device name: rx, tx)
        """
        if not hasattr(self, 'network'):
            return {}
        res_dict = {}
        self.network = self.network[2:]
        for device in self.network:
            info = {}
            device = device.split()
            info['rx'] = self._format_number(device[1], unit)
            info['tx'] = self._format_number(device[9], unit)
            res_dict[device[0][:-1]] = info
        return res_dict







