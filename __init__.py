

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from . import RELAYplate as RELAY
import octoprint.plugin
from octoprint.events import Events, eventManager

##############################################################################    
###################### Set address of RELAYplate below: ######################
ppADDR=0
##############################################################################

relays = ['Nozzle fan', 'Driver fan']

class PiPlatesRelayPlugin(octoprint.plugin.EventHandlerPlugin, octoprint.plugin.StartupPlugin,octoprint.plugin.ShutdownPlugin):
    
    def __init__(self):
        self._status = ['OFF'] * 7
        super().__init__()

    def reset(self):
        """reset all relays to OFF"""
        RELAY.RESET(ppADDR)                                                         
        for i in range(7):
            self._status[i]='OFF'

    
    def on_after_startup(self):
        """reset all relays to OFF"""
        self.reset()

    def on_shutdown(self):
        """reset all relays to OFF"""
        self.reset()

    def on_event(self, event, payload):
        if event == Events.PRINT_STARTED or event == Events.PRINT_RESUMED:
            for i in range(len(relays)):
                RELAY.relayON(ppADDR,i+1)
                self._status[i]='ON'
        elif event == Events.PRINT_CANCELLED or event == Events.PRINT_DONE:
            for i in range(len(relays)):
                RELAY.relayOFF(ppADDR,i+1)
                self._status[i]='OFF'


__plugin_name__ = "Pi-Plates relay"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Control piplates relays"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = PiPlatesRelayPlugin()
