from yowsup.stacks import YowStackBuilder
from layer import SendLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.auth import YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.network import YowNetworkLayer



class YowsupSendStack(object):
    def __init__(self, credentials, encryptionEnabled = False):
        stackBuilder = YowStackBuilder()


        self.stack = stackBuilder.pushDefaultLayers(encryptionEnabled).push(SendLayer).build()
        # self.stack.setProp(YowAuthenticationProtocolLayer.PROP_PASSIVE, True)
        self.stack.setCredentials(credentials)

    def start(self):
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            self.stack.loop()
        except AuthError as e:
            print("Authentication Error: %s" % e.message)
