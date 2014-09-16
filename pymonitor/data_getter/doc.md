#data_getter
This package only access data and never modify any of them.
##Structure
```
--data_getter
    |
    --base.py - InfoBase . common interface of data_getter.
    |
    --disk.py - disk io-stats and parttions's(include swap) information.
    |
    --mem.py - memory and swap information.
    |
    --network.py - received and sent bytes of each net device.
    |
    --ports.py - view each collection and its process information with some basic calculation.
    |
    --processes.py - view detail of each process include cpu and mem info.
    |
    --sysinfo.py - distribution, arch, cores, uptime, etc.
    |
    --cpu.py - usage percent, loadavg , etc.
```
##Usage
just implement it and call `get_as*` method
```
from pymonitor.data_getter.cpu import CPU
c = CPU()
c.get_asdict()
```

##Common Interface

###InfoBase.get_asdict()
Return a python dict, access it by key.    
For example, to access cpu `LoadAVG` info:
```python
result = InfoBase.get_asdict()
print result['LoadAVG']
```
###InfoBase.get_asjson()
Return a list of (property, value) list.
For example, to access cpu `LoadAVG` info:
```python
result = InfoBase.get_aslist()
for i in result:
    if i[0] == 'LoadAVG':
    print i[1]
```
###InfoBase.get_aslist()
Return dumped InfoBase.get_asdict() result.
Return directly to web request.



