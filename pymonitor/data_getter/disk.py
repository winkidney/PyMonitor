#!/usr/bin/env python
# coding:utf-8
# disk - 
# author : winkidney - 14-9-16
__author__ = 'winkidney'

"""
docs from kernel.org
What:		/proc/diskstats
Date:		February 2008
Contact:	Jerome Marchand <jmarchan@redhat.com>
Description:
        The /proc/diskstats file displays the I/O statistics
        of block devices. Each line contains the following 14
        fields:
         1 - major number
         2 - minor mumber
         3 - device name
         4 - reads completed successfully
         5 - reads merged
         6 - sectors read
         7 - time spent reading (ms)
         8 - writes completed
         9 - writes merged
        10 - sectors written
        11 - time spent writing (ms)
        12 - I/Os currently in progress
        13 - time spent doing I/Os (ms)
        14 - weighted time spent doing I/Os (ms)
        For more details refer to Documentation/iostats.txt
"""



import logging

from .base import InfoBase


class Disk(InfoBase):

    def __init__(self):
        try:
            self.network = open('/proc/diskstats', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read /proc/diskstats !")

    def get_asdict(self, dev=None, unit='byte'):
        result = {}
        columns_disk = ['m', 'mm', 'dev', 'reads', 'rd_mrg', 'rd_sectors',
                    'ms_reading', 'writes', 'wr_mrg', 'wr_sectors',
                    'ms_writing', 'cur_ios', 'ms_doing_io', 'ms_weighted']

        columns_partition = ['m', 'mm', 'dev', 'reads', 'rd_sectors', 'writes', 'wr_sectors']

        lines = self.network
        for line in lines:
            if line == '':
                continue
            split = line.split()
            if len(split) == len(columns_disk):
                columns = columns_disk
            elif len(split) == len(columns_partition):
                columns = columns_partition
            else:
                # No match
                continue

            data = dict(zip(columns, split))
            if dev != None and dev != data['dev']:
                continue
            for key in data:
                if key != 'dev':
                    data[key] = int(data[key])
            result[data['dev']] = data

        return result