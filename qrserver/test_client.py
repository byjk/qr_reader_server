from time import sleep
from kivy.lib import osc
import sys

serviceport = 3000
activityport = 3001


if __name__ == '__main__':
    osc.init()
    # oscid = osc.listen(ipAddr='0.0.0.0', port=activityport)
    # osc.bind(oscid, some_api_callback, '/some_api')
    m = 'ping'
    if len(sys.argv) > 1:
        m = sys.argv[1]
    osc.sendMsg('/qr_api', [m], ipAddr='127.0.0.1', port=serviceport)