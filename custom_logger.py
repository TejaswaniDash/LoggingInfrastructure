"""
GENERIC METHOD THAT WE GONNA USE FOR ALL CLASSES
"""

import inspect

import logging

def customLogger(logLevel): #with the help logLevel we can call the level of logs

    # Gets the name of the class / method from where this message is called

    loggerName = inspect.stack()[1][2]
    looger = logging.getlogger(loggerName)

    #By default, log all messages
    logger.setLevel(logging.DEBUG)
    # provide the logger name as the filehandler
    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode = 'w')
#mode "w" because we don't want append to our file
    fileHandler.setLevel(loglevel)
    #to set the log level whatever we providing

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(form)
    #add the Handler to the logger
    logger.addHandler(fileHandler)


    return logger







