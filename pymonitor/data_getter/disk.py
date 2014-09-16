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
import re
import psutil

from .base import InfoBase


class Disk(InfoBase):

    def __init__(self):
        pass

    def get_asdict(self, dev=None):
        res_dict = {}
        res_dict['DiskStats'] = self._get_diskstats(dev)
        res_dict['SwapInfo'] = self._get_swap_info()
        res_dict['MountedInfo'] = self._get_mounted_info()
        res_dict['StorageStatus'] = self._get_partions()
        return res_dict

    @staticmethod
    def _get_fs_usage(mountpoint):
        """
        Return dist usage dict by given mountpoion str.
        :param mountpoint: string stands for mountpoint
        :type mountpoint:str
        :return: dict
        """
        column_list = ['total', 'used', 'free', 'percent']
        result = list(psutil.disk_usage(mountpoint))
        return dict(zip(column_list, result))

    def _get_partions(self):
        column_list = ['device', 'mountpoint', 'fstype', 'opts']
        disks = psutil.disk_partitions()
        res_list = []
        for disk in disks:
            disk_dict = dict(zip(column_list, disk))
            disk_dict['SpaceInfo'] = self._get_fs_usage(disk_dict['mountpoint'])
            res_list.append(disk_dict)
        return res_list

    def _get_swap_info(self):
        try:
            self.swaps = open('/proc/swaps', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read /proc/swaps !")
            return {}
        result_dict = {}
        column_swap = ['Filename', 'Type', 'Size', 'Used', 'Priority']
        for line in self.swaps[1:]:
            result = dict(zip(column_swap, line.split()))
            result_dict[result['Filename']] = result
        return result_dict

    def _get_mounted_info(self):
        try:
            self.mtab = open('/etc/mtab', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read /proc/mtab !")
            return {}
        result_dict = {}
        column_mounted = ['Filename', 'MountedDir', 'FileSystem', 'Option', 'DumpOption', 'FSCKOption']
        for line in self.mtab:
            result = dict(zip(column_mounted, line.split()))
            result_dict[result['Filename']] = result
        return result_dict

    def _get_diskstats(self, dev):
        """
        Get all info from /proc/diskstats
        :param dev: exclude device list, each element is a regx str.
        :type dev: list
        :return: dict
        """
        try:
            self.diskstats = open('/proc/diskstats', 'r').readlines()
        except IOError:
            logging.warning("Couldn't read /proc/diskstats !")
            return {}
        result = {}
        columns_disk = ['m', 'mm', 'dev', 'reads', 'rd_mrg', 'rd_sectors',
                        'ms_reading', 'writes', 'wr_mrg', 'wr_sectors',
                        'ms_writing', 'cur_ios', 'ms_doing_io', 'ms_weighted']

        columns_partition = ['m', 'mm', 'dev', 'reads', 'rd_sectors', 'writes', 'wr_sectors']

        lines = self.diskstats
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
            if dev:
                for regx in dev:
                    if re.search(regx, data['dev']):
                        continue
            for key in data:
                if key != 'dev':
                    data[key] = int(data[key])
            result[data['dev']] = data

        return result

    #todo : add io status monitor method