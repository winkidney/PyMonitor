#!/usr/bin/env python
# coding:utf-8
# cpu - 
# author : winkidney - 14-9-15
__author__ = 'winkidney'

import logging

from .base import InfoBase


class CPU(InfoBase):

    def __init__(self):
        try:
            self.cpuinfo = open('/proc/stat', 'r').readlines()
            self.loadavg = open('/proc/loadavg', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read CPUINFO !")

    def get_asdict(self):
        if not hasattr(self, 'cpuinfo') or not hasattr(self, 'loadavg'):
            return {}
        res_dict = {}
        for line in self.cpuinfo:
            if line.startswith('cpu'):
                result = line.split()
                res_dict[result[0]] = {
                    'user': int(result[1]),
                    'nice': int(result[2]),
                    'system': int(result[3]),
                    'idle': int(result[4]),
                    'wait': int(result[5]),
                }
        res_dict['loadavg'] = [float(i) for i in self.loadavg[0].split()[:2]]
        return res_dict
