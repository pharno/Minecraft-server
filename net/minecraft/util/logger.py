import logging


logger = logging.getLogger('Minecraft')
filelogger = logging.FileHandler('server.log')
consolelogger = logging.StreamHandler()


formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')


filelogger.setFormatter(formatter)
consolelogger.setFormatter(formatter)

logger.addHandler(consolelogger)
logger.addHandler(filelogger)
logger.setLevel(logging.DEBUG)