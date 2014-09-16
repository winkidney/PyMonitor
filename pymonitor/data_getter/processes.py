#!/usr/bin/env python
# coding:utf-8
# Processes - 
# author : winkidney - 14-9-17
import logging

__author__ = 'winkidney'

import psutil

from .base import InfoBase


class Processes(InfoBase):

    def __init__(self):
        pass

    def get_asdict(self):
        res_dict = {}
        res_dict['PIDList'] = psutil.pids()
        res_dict['PROCSINFO'] = self._get_procs_info(res_dict['PIDList'])
        return res_dict

    def _get_processes(self, pids):
        processes = []
        for pid in pids:
            process = self._get_process(pid)
            if process:
                processes.append(process)
        return processes

    def _get_procs_info(self, pids):
        """
        The process detail include such columns
        ['pid', 'ppid', 'name', 'create_time',
                       'username', 'io_counters', 'cpu_percent', 'memory_info']
        :param pids: list of pid
        :return:
        """
        procs_list = self._get_processes(pids)
        column_list = ['pid', 'ppid', 'name', 'create_time',
                       'username', 'io_counters', 'cpu_percent', 'memory_info']
        result_list = []
        for process in procs_list:
            if process:
                try:
                    p_dict = process.as_dict(attrs=column_list)
                    if p_dict['memory_info']:
                        p_dict['memory_info'] = \
                            dict(zip(p_dict['memory_info']._fields,
                                     list(p_dict['memory_info'])))
                    if p_dict['io_counters']:
                        p_dict['io_counters'] = dict(zip(p_dict['io_counters']._fields,
                                                         list(p_dict['io_counters'])))
                    result_list.append(p_dict)
                except psutil.AccessDenied:
                    logging.warning('Access Denied! when access info of pid [%s]' % process.pid)

        return result_list

    def _get_process(self, pid):
        """
        Return a psutil.Process object
        :param pid:
        :type pid: int
        :return: psutil.Porcess
        """
        try:
            return psutil.Process(pid)
        except psutil.NoSuchProcess:
            logging.warning('No such process of pid [%s]' % pid)
            return None










