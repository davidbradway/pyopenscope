# example_script.py

from pyopenscope import OpenScope
o=OpenScope('http://localhost:42135')

o.deviceEnumerate()

o.oscGetCurrentState(1)

o.awgStop(channel=1)

o.awgGetCurrentState(channel=1)

o.awgSetRegularWaveform(channel=1, signalType='sine', signalFreq=1000000, vpp=3000, vOffset=0)

o.awgRun(channel=1)

o.awgGetCurrentState(channel=1)

o.triggerSingle(1)

o.oscRead(channel=1, acqCount=1)
