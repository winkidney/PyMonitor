#!/usr/bin/env python
# coding:utf-8
# ports - 
# author : winkidney - 14-9-17
import logging
import os
import psutil

from pymonitor.data_getter.base import InfoBase

__author__ = 'winkidney'


class Ports(InfoBase):

    def __init__(self):
        if os.getuid() != 0:
            logging.warning('Not run as root, some connections info may not be access!')
        self.pids_names = {}

    def get_asdict(self):
        res_dict = {}

        connections = psutil.net_connections(kind='inet')
        cons_dict_list = []
        status_counters = {}
        for connection in connections:
            if not status_counters.get(connection.status):
                status_counters[connection.status] = 1
            else:
                status_counters[connection.status] += 1
            connection_d = dict(zip(connection._fields, tuple(connection)))
            connection_d['name'] = self.pid2name(connection_d['pid'])
            cons_dict_list.append(connection_d)


        res_dict['Connections'] = cons_dict_list
        res_dict['ConCount'] = len(cons_dict_list)
        res_dict['ConStatus'] = status_counters

        return res_dict
    def pid2name(self, pid):
        if not pid:
            return
        pname = self.pids_names.get(pid)
        if pname:
            pass
        else:
            try:
                pname = psutil.Process(pid).name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                logging.warning('Can not access [%s] s process name!' % pid)
        self.pids_names[pid] = pname
        return pname