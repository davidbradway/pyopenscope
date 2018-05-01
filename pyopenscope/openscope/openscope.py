# -*- coding: utf-8 -*-

class OpenScope:
    """
    Library designed to communicate with the OpenScope
    JSON requests

    Requires requests, re, json, numpy, and pprint libraries to be installed

    :param str url: URL of the OpenScope
                (e.g. 'http://localhost:42135' or 'http://10.190.76.108')

    Contributors: Nick Bottenus, David Bradway
    """

    ###################################################################
    # Initialization
    ###################################################################
    def __init__(self, url):
        """
        Initialize
        
        :param str url: A string representing the OpenScope's url
        """
        if url is not None:
            if(isinstance(url, str)):
                self.url = url
        
        import pprint
        self.pp = pprint.PrettyPrinter(indent=4)


    def close(self):
        """
        Close
        """

    ###################################################################
    # Commands
    ###################################################################
    
    def debugPrint(self, mode='off'):
        """
        Set the desired device debug print status

        :param 'off'/'on' mode: desired device debug print status
        """
        import requests
        payload = {'debugPrint':mode}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)
        self.mode = self.jsonout['debugPrint']


    def deviceEnumerate(self):
        """
        Enumerate all device info.

        This should return static information about the device. 
        Dynamic data should be retrieved using getters.
        """
        import requests
        payload = {"device": [{"command": "enumerate"}]}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)


    def oscGetCurrentState(self, channel=1):
        """
        Get the current state of the instrument's channel

        :param channel: which channel to get current state
        """
        import requests
        payload = {'osc': {str(channel): [{"command": "getCurrentState"}]}}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)


    def oscRead(self, channel=1, acqCount=1):
        """
        Read data from the device. Data will be returned if the device 
        acqCount is greater or equal to the command acqCount. If the device
        acqCount is less than the command acqCount the device responds with 
        its trigger status and optionally a estimated time before a new buffer 
        will be available.Data is returned in chunked transfer format. The 
        first chunk of data is a JSON object that describes the following chunk
        of binary data. The binary data type and resolution are defined in the
        device enumeration and units are in mV. The first byte in the binary 
        data corresponds to the first sample in the buffer (the earliest sample
        chronologically).

        :param channel: which channel to get current state
        :param acqCount: The acquisition count
        """
        import requests
        import re
        import json
        import numpy
        payload = {'osc': {str(channel): [{'command': 'read', 'acqCount': str(acqCount)}]}}
        r = requests.post(self.url, json=payload)
        result = re.split(b'\r\n',r.content)
        # self.result = result
        if len(result) > 2:
            # Decode bytes, and convert single quotes to double quotes for valid JSON
            if result[1] != b'':
                str_json = result[1].decode('ASCII').replace("'", '"')
                # Load the JSON to a Python list & pretty print formatted JSON
                self.jsonout = json.loads(str_json)
                self.pp.pprint(self.jsonout)

                data = result[4]

                SampleFreq = self.jsonout['osc']['1'][0]['actualSampleFreq']/1000

                mvolts=numpy.zeros(len(data)//2)
                for i in range(0, len(data)-2, 2):
                    mvolts[i//2] = int.from_bytes(data[i:i+2], byteorder='little', signed=True)

                self.volts = mvolts / 1000
                self.t = numpy.arange(len(volts)) / SampleFreq
            else:
                print(result[0])
        else:
            print(result[0])

    def triggerSingle(self, channel=1):
        """
        Arm the specified trigger and do not re-arm the trigger after a successful acquisition.

        :param channel: which trigger channel to arm
        """
        import requests
        payload = {"trigger":{str(channel):[{"command":"single"}]}}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)


    def awgGetCurrentState(self, channel=1):
        """
        Get the current state of the instrument's channel

        :param channel: which channel to get current state
        """
        import requests
        payload = {'awg': {str(channel): [{"command": "getCurrentState"}]}}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)


    def awgStop(self, channel=1):
        """
        Stop the arbitrary waveform generator channel(s).

        :param channel: which waveform generator channel to stop
        """
        import requests
        payload = {"awg":{str(channel):[{"command":"stop"}]}}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)
  

    def awgSetRegularWaveform(self, channel=1, signalType='sine', signalFreq=1000000, vpp=3000, vOffset=0):
        """
        Set the parameters of the arbitrary waveform generator channel(s) to output a regular waveform.

        :param channel: which waveform generator channel to set
        :param signalType: (String) - The waveform type: “sine”, “square”, “triangle”, “dc”, “sawtooth”, “arbitrary”, or “none”.
        :param signalFreq: (Integer) - The signal frequency in mHz.
        :param vpp: (Integer) - The peak-to-peak voltage in mV.
        :param vOffset: (Integer) - The voltage offset in mV.
        """
        import requests
        payload = {"awg":{str(channel):[{"command":"setRegularWaveform",
                                "signalType":signalType,
                                "signalFreq":signalFreq,
                                "vpp":vpp,
                                "vOffset":vOffset}]}}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)


    def awgRun(self, channel=1):
        """
        Run the arbitrary waveform generator channel(s).

        :param channel: which waveform generator channel to start
        """
        import requests
        payload = {"awg":{str(channel):[{"command":"run"}]}}
        r = requests.post(self.url, json=payload)
        self.jsonout = r.json()
        self.pp.pprint(self.jsonout)
