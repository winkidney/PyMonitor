#!/usr/bin/env python
# coding:utf-8
# mem - 
# author : winkidney - 14-9-15
__author__ = 'winkidney'

import re
import logging

from .base import InfoBase

MEMTOTAL_REGX = re.compile('(MemTotal)\:.*?(\d{1,50})')
MEMFREE_REGX = re.compile('(MemFree)\:.*?(\d{1,50})')
BUFFERS_REGX = re.compile('(Buffers)\:.*?(\d{1,50})')
CACHED_REGX = re.compile('(Cached)\:.*?(\d{1,50})')

SWAPTOTAL_REGX = re.compile('(SwapTotal)\:.*?(\d{1,50})')
SWAPFREE_REGX = re.compile('(SwapFree)\:.*?(\d{1,50})')


class Memory(InfoBase):
    """
    UNIT: KB
    """
    def __init__(self):
        pass

    def get_asdict(self):
        try:
            self.meminfo = open('/proc/meminfo', 'r').read()
        except IOError:
            logging.warning("Couldn't read /proc/meminfo !")
            return {}
        res_dict = {}
        res_dict['MemTotal'] = re.search(MEMTOTAL_REGX, self.meminfo)
        res_dict['MemFree'] = re.search(MEMFREE_REGX, self.meminfo)
        res_dict['Buffers'] = re.search(BUFFERS_REGX, self.meminfo)
        res_dict['Cached'] = re.search(CACHED_REGX, self.meminfo)

        res_dict['SwapTotal'] = re.search(SWAPTOTAL_REGX, self.meminfo)
        res_dict['SwapFree'] = re.search(SWAPFREE_REGX, self.meminfo)
        result_dict = {}
        for item in res_dict.items():
            result_dict[item[0]] = int(item[1].group(2))
        return result_dict