from net.minecraft.server.MinecraftServer import MinecraftServer

import signal
import traceback
import logging
from net.minecraft.util.logger import logger

mc = MinecraftServer()
log = logger
def handler(signum, frame):
    print signum
    print "stopping"
    mc.stopServer()

#signal.signal(signal.SIGINT, handler)


try:
    mc.startServer()
except:
    log.critical(traceback.format_exc())
finally:
    mc.stopServer()