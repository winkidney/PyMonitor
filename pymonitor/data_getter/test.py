#!/usr/bin/env python
# coding:utf-8
# test.py - 
# author : winkidney - 14-9-18

import unittest
from .network import Network
from .cpu import CPU
from .mem import Memory
from .ports import Ports
from .processes import Processes
from .sysinfo import SysInfo
from .disk import Disk

class TestDateGetter(unittest.TestCase):

    def setUp(self):
        pass

    def test_NetWork_return(self):
        target = Network()
        self.assertTrue(isinstance(target.get_asjson(), str))
        self.assertTrue(isinstance(target.get_asdict(), dict))

    def test_CPU_return(self):
        target = CPU()
        self.assertTrue(isinstance(target.get_asjson(), str))
        self.assertTrue(isinstance(target.get_asdict(), dict))

    def test_Memory_return(self):
        target = Memory()
        self.assertTrue(isinstance(target.get_asjson(), str))
        self.assertTrue(isinstance(target.get_asdict(), dict))

    def test_Ports_return(self):
        target = Ports()
        self.assertTrue(isinstance(target.get_asjson(), str))
        self.assertTrue(isinstance(target.get_asdict(), dict))

    def test_Processes_return(self):
        target = Processes()
        self.assertTrue(isinstance(target.get_asjson(), str))
        self.assertTrue(isinstance(target.get_asdict(), dict))

    def test_SysInfo_return(self):
        target = SysInfo()
        self.assertTrue(isinstance(target.get_asjson(), str))
        self.assertTrue(isinstance(target.get_asdict(), dict))

    def test_Disk_return(self):
        target = Disk()
        self.assertTrue(isinstance(target.get_asjson(), str))
        self.assertTrue(isinstance(target.get_asdict(), dict))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()