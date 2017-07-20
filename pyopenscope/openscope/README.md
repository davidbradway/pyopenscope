## OpenScope

Multi-purpose OpenScope device

### Python interface
A python module is included to JSON HTTP Get requests

On Windows, you will need the drivers installed

First, import the library module and create an instance with shorthand 'o'.
``` python
import pyopenscope
o=pyopenscope.OpenScope('http://localhost:42135')
```
The following functions are included (see openscope.py for more detailed documentation):

| Commands | Description |
| ------- | ----------- |
| `o.init(url)`|Initialize the OpenScope at the given URL|
| `o.close()`| Close |
| `o.debugPrint(mode='off')`| Set the desired device debug print status|
| `o.deviceEnumerate()`| Enumerate all device info.|
| `o.oscGetCurrentState(channel=1)`| Get the current state of the instrument's channel|
| `o.triggerSingle(channel=1)`| Arm the specified trigger and do not re-arm the trigger after a successful acquisition.|
| `o.awgGetCurrentState(channel=1)`| Get the current state of the instrument's channel |
| `o.awgStop(channel=1)`| Stop the arbitrary waveform generator channel(s). |
| `o.awgSetRegularWaveform(channel=1, signalType='sine', signalFreq=1000000, vpp=3000, vOffset=0)`| Set the parameters of the arbitrary waveform generator channel(s) to output a regular waveform.|
| `o.awgRun(channel=1)`| Run the arbitrary waveform generator channel(s).|
