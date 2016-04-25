from time import sleep
from kivy.lib import osc
import os, ntpath


class qrserver:
    serviceport = 3000
    scriptdir = './scripts'
    # activityport = 3001
    _oscid = 0
    _params = ''
    _script = ''
    
    def __init__(self, **kwargs):
        osc.init()
        self._oscid = osc.listen(ipAddr='0.0.0.0', port=self.serviceport)
        osc.bind(self._oscid, self.qr_callback, '/qr_api')
        
    def qr_callback(self, message, *args):
        m = str(message[2])
        print("got a message! %s" % m)
        if m.startswith('qr://'):
            qrdata = m[5:]
            # print(qrdata)
            if qrdata.startswith('S4A') or qrdata.startswith('S4D') or qrdata.startswith('S4O'):
                self._params = qrdata
            elif qrdata.startswith("script:"):
                script = ntpath.basename(qrdata[7:])
                script = os.path.join(self.scriptdir,script)
                if os.path.isfile(script):
                    self._script = script
            if self._script != '' and self._params != '':
                s = self._script + ' ' + self._params
                print('calling script: "'+s+'"')                
                os.system(s)
                
                
    def Run(self):
        while True:
            osc.readQueue(self._oscid)
            sleep(.10)
            
if __name__ == '__main__':
    srv = qrserver()
    srv.Run()
