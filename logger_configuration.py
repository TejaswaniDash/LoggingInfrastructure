"""
LOGGER DEMO FROM A CONFIGURATION FILE
"""
#create a logger
import logging

class LoggerDemoConf():
    def testLog(self):
# create a logger
#load all the configuration file so we can read all the configruation
        logging.config.fileConfig('loggingConfDemo.conf')
#logger object-> getLogger()
        logger = logging.getLogger(LoggerDemoConf.__name__)

#LOGGING MESSAGES

        logger.debug(" Debug message ")
        logger.info(" Info message ")
        logger.warning(" Warning message ")
        logger.error(" Error message ")
        logger.critical(" Critical message ")

demo = LoggerDemoConf()
demo.testLog()
