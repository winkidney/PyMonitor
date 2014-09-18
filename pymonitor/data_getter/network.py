#!/usr/bin/env python
# coding:utf-8
# net - 
# author : winkidney - 14-9-16
import datetime
import time
import psutil

__author__ = 'winkidney'


from .base import InfoBase


class Network(InfoBase):

    def __init__(self):
        pass

    def get_asdict(self):
        """
        only tested on by ubuntu!
        :return: a dict{device name: device_detail}
        device_detail : a dict -
            {bytes_sent:'', bytes_recv:'', packets_sent:'', packets_recv: '', etc...}
        """
        res_dict = self._get_basic()
        rates = self._get_current_rate()
        for key in res_dict:
            res_dict[key]['rates'] = rates[key]
        return res_dict

    def _get_basic(self):

        res_dict = {}
        result = psutil.net_io_counters(pernic=True)
        for key in result:
            res_dict[key] = dict(zip(result[key]._fields, result[key]))
        return res_dict

    def _get_current_rate(self, delay=1):
        """
        Sleep given delay seconds and return the network recv/send rate.
        :param delay: delay seconds for calculating data transfer speed.
        :type delay: int
        :tpye delay: float
        :return: rate_dict  {device_name:{'rate_recv': rate_recv, 'rete_send': rate_send}}
        """
        rate_dict = {}
        data_before, time_before = self._get_basic(), datetime.datetime.now()
        time.sleep(delay)
        data_after, time_after = self._get_basic(), datetime.datetime.now()
        time_delta = (time_after - time_before).microseconds / float(1000*1000)
        for key in data_before:
            rate_dict[key] = {}
            rate_dict[key]['rate_send'] = float((data_after[key]['bytes_sent'] - data_before[key]['bytes_sent']))/time_delta
            rate_dict[key]['rate_recv'] = float((data_after[key]['bytes_recv'] - data_before[key]['bytes_recv']))/time_delta
        return rate_dict







