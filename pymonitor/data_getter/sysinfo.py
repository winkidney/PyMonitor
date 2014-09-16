#!/usr/bin/env python
# coding:utf-8
# sysinfo - 
# author : winkidney - 14-9-16
__author__ = 'winkidney'

import logging
import multiprocessing

from .base import InfoBase
import platform
import socket

class SysInfo(InfoBase):

    def __init__(self):
        pass

    def get_asdict(self):
        res_dict = {}
        res_dict['Distribution'] = self._get_dist()
        res_dict['Arch'] = platform.architecture()
        res_dict['Cores'] = multiprocessing.cpu_count()
        res_dict['Kernel'] = platform.release()
        res_dict['Uname'] = platform.uname()
        res_dict['Uptime'] = self._get_uptime()
        res_dict['Hostname'] = socket.gethostname()
        return res_dict

    @staticmethod
    def _get_dist():
        column_dist = ['Distribution', 'Version', 'name']
        return dict(zip(column_dist, platform.linux_distribution()))

    def _get_uptime(self):
        try:
            self.uptime = open('/proc/uptime', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read /proc/uptime" )
        return float(self.uptime[0].split()[0])