# // Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
# // Jad home page: http://www.kpdus.com/jad.html
# // Decompiler options: packimports(3) braces deadcode fieldsfirst 
# 
# package net.minecraft.src;
# 
# import java.io.IOException;
# import java.net.ServerSocket;
# import java.net.Socket;
# import java.util.HashMap;
# import net.minecraft.server.MinecraftServer;
# 
# // Referenced classes of package net.minecraft.src:
# //            NetworkListenThread, NetLoginHandler

import threading
import time
from net.minecraft.util.logger import logger
from net.minecraft.util.make_tasklet import make_tasklet

@make_tasklet
class NetworkAcceptThread():
    def __init__(self,listenthread, name, minecraftserver):
        self.netWorkListener = listenthread
        self.mcServer = minecraftserver

    def run(self):
        while True:
            try:
                sock,inetaddress = self.netWorkListener.serverSocket.accept()
                logger.info("got connection: %s:%s" % inetaddress)
                if inetaddress in self.netWorkListener.sockets and ((time.clock() - self.netWorkListener.sockets[inetaddress]) < 0.500):
                    self.netWorkListener.sockets[inetaddress] = time.clock()
                    sock.close()
                    logger.info("closing connection: %s:%s" % inetaddress)
                    return
                self.netWorkListener.sockets[inetaddress] = time.clock()
    #                 NetLoginHandler netloginhandler = new NetLoginHandler(mcServer, socket, (new StringBuilder()).append("Connection #").append(NetworkListenThread.func_712_b(netWorkListener)).toString());
    #                 NetworkListenThread.func_716_a(netWorkListener, netloginhandler);
    #             }
            except IOError as exception:
                logger.info("%s" % (exception))
                pass
