# // Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
# // Jad home page: http://www.kpdus.com/jad.html
# // Decompiler options: packimports(3) braces deadcode fieldsfirst 
# 
# package net.minecraft.src;
# 
# import java.io.*;
# import java.util.Properties;
from net.minecraft.util.Properties import Properties
from net.minecraft.util.logger import logger

# 
class PropertyManager:

    def __init__(self,fil):
        self.logger = logger
        self._serverProperties = Properties()
        try:
            self._serverPropertiesFile = fil
            self._serverProperties.load(open(self._serverPropertiesFile,"rw"))
        except Exception as exception:
            self.logger.warn("Failed to load %s: %s" % (fil,exception))
            self.generateNewProperties()

    def generateNewProperties(self):
        self.logger.info("Generating new properties file")
        self.saveProperties()

    def saveProperties(self):
        try:
            self._serverProperties.store(open(self._serverPropertiesFile,"rw"), "Minecraft server properties")
        except Exception as ex:
            self.logger.warn("Failed to save %s: %s" % (fil,exception))
            self.generateNewProperties()            

    def getPropertiesFile(self):
        return open(self._serverPropertiesFile,"rw")

    def getStringProperty(self,key,default):
        if not self._serverProperties.containsKey(key):
            self._serverProperties.setProperty(key,default)
            self.saveProperties()

        return self._serverProperties.getProperty(key)


    def getIntProperty(self,key,default):
        if not self._serverProperties.containsKey(key):
            self._serverProperties.setProperty(key,default)
            self.saveProperties()
        try:
            val = self._serverProperties.getProperty(key)
            return int(val)
        except:
            self.logger.warn("invalid value for %s: %s" %(key,val))
            return default

    def getBooleanProperty(self,key,default):
        if not self._serverProperties.containsKey(key):
            self._serverProperties.setProperty(key,default)
            self.saveProperties()
        try:
            val = self._serverProperties.getProperty(key)
            return bool(val)
        except:
            self.logger.warn("invalid value for %s: %s" %(key,val))
            return default

