# // Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
# // Jad home page: http://www.kpdus.com/jad.html
# // Decompiler options: packimports(3) braces deadcode fieldsfirst 
# 
# package net.minecraft.src;
# 
# import java.io.IOException;
# import java.net.*;
# import java.util.ArrayList;
# import java.util.HashMap;
# import java.util.logging.Level;
# import java.util.logging.Logger;
# import net.minecraft.server.MinecraftServer;
# 
# // Referenced classes of package net.minecraft.src:
# //            NetworkAcceptThread, NetLoginHandler, NetworkManager, NetServerHandler
#
from net.minecraft.src.NetworkAcceptThread import NetworkAcceptThread


from net.minecraft.util.logger import logger


import socket

class NetworkListenThread:

    def __init__(self,minecraftserver,inetaddress, port):
        self.isListening = False
        self.field_997_f = 0;
        self.pendingConnections = []
        self.playerList = []
        self.sockets = {}
        self.mcServer = minecraftserver
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((inetaddress,port))
        self.serverSocket.listen(5)
        self.isListening = True
        self.networkAcceptThread = NetworkAcceptThread(self,"Listen thread",minecraftserver)
        self.networkAcceptThread.start()

# 
#     public void func_35505_a(Socket socket)
#     {
#         InetAddress inetaddress = socket.getInetAddress();
#         synchronized(sockets)
#         {
#             sockets.remove(inetaddress);
#         }
#     }
# 
#     public void addPlayer(NetServerHandler netserverhandler)
#     {
#         playerList.add(netserverhandler);
#     }
# 
#     private void addPendingConnection(NetLoginHandler netloginhandler)
#     {
#         if(netloginhandler == null)
#         {
#             throw new IllegalArgumentException("Got null pendingconnection!");
#         } else
#         {
#             pendingConnections.add(netloginhandler);
#             return;
#         }
#     }
# 
#     public void handleNetworkListenThread()
#     {
#         for(int i = 0; i < pendingConnections.size(); i++)
#         {
#             NetLoginHandler netloginhandler = (NetLoginHandler)pendingConnections.get(i);
#             try
#             {
#                 netloginhandler.tryLogin();
#             }
#             catch(Exception exception)
#             {
#                 netloginhandler.kickUser("Internal server error");
#                 logger.log(Level.WARNING, (new StringBuilder()).append("Failed to handle packet: ").append(exception).toString(), exception);
#             }
#             if(netloginhandler.finishedProcessing)
#             {
#                 pendingConnections.remove(i--);
#             }
#             netloginhandler.netManager.wakeThreads();
#         }
# 
#         for(int j = 0; j < playerList.size(); j++)
#         {
#             NetServerHandler netserverhandler = (NetServerHandler)playerList.get(j);
#             try
#             {
#                 netserverhandler.handlePackets();
#             }
#             catch(Exception exception1)
#             {
#                 logger.log(Level.WARNING, (new StringBuilder()).append("Failed to handle packet: ").append(exception1).toString(), exception1);
#                 netserverhandler.kickPlayer("Internal server error");
#             }
#             if(netserverhandler.connectionClosed)
#             {
#                 playerList.remove(j--);
#             }
#             netserverhandler.netManager.wakeThreads();
#         }
# 
#     }
# 
#     static ServerSocket getServerSocket(NetworkListenThread networklistenthread)
#     {
#         return networklistenthread.serverSocket;
#     }
# 
#     static HashMap func_35504_b(NetworkListenThread networklistenthread)
#     {
#         return networklistenthread.sockets;
#     }
# 
#     static int func_712_b(NetworkListenThread networklistenthread)
#     {
#         return networklistenthread.field_977_f++;
#     }
# 
#     static void func_716_a(NetworkListenThread networklistenthread, NetLoginHandler netloginhandler)
#     {
#         networklistenthread.addPendingConnection(netloginhandler);
#     }
# 
    def shutdown(self):
        logger.info("closing NetworkListenThread")
        self.isListening = False
        self.serverSocket.close()