## Python interface for OpenScope

### Installation

Installation allows you to use this code from any directory instead of just the pyopenscope directory. 

To install the package, run:

```
python setup.py develop
```

The `develop` option makes a symlink to the code so that as it changes you don't need to reinstall. For a fixed installation, you can use `install` instead.

This will install `pprint`, `requests`, and `numpy` as needed

To uninstall, run:

```
python setup.py develop --uninstall
```

### Usage

To use the package, simply run:

```python
import pyopenscope
```

Alternatively, you can import the module into the base namespace using
```python
from pyopenscope import *
```

The module described below is accessible as an object within pyopenscope. To connect, the controlling computer should be connected to the same network as the OpenScope

### Module

#### OpenScope
```python
from pyopenscope import OpenScope
o=OpenScope('http://localhost:42135')
o.deviceEnumerate()
o.oscGetCurrentState(1)
o.awgStop(channel=1)
o.awgGetCurrentState(channel=1)
o.awgSetRegularWaveform(channel=1, signalType='square', signalFreq=1000000, vpp=3000, vOffset=0)
o.awgRun(channel=1)
o.awgGetCurrentState(channel=1)
o.triggerSingle(1)
o.oscRead(channel=1, acqCount=1)


```
