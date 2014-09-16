#!/usr/bin/env python
# coding:utf-8
# cpu - 
# author : winkidney - 14-9-15
__author__ = 'winkidney'

import logging
import psutil

from .base import InfoBase


class CPU(InfoBase):

    def __init__(self):
        pass

    def get_asdict(self):
        try:
            self.cpuinfo = open('/proc/stat', 'r').readlines()
            self.loadavg = open('/proc/loadavg', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read /proc/stat and /proc/loadavg !")
            return {}
        res_dict = {}
        for line in self.cpuinfo:
            if line.startswith('cpu'):
                result = line.split()
                res_dict[result[0]] = {
                    'User': int(result[1]),
                    'Nice': int(result[2]),
                    'System': int(result[3]),
                    'Idle': int(result[4]),
                    'Wait': int(result[5]),
                }
        res_dict['LoadAVG'] = [float(i) for i in self.loadavg[0].split()[:2]]
        res_dict['CpuPercent'] = psutil.cpu_percent()
        return res_dict
