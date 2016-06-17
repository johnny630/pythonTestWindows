# -*- coding: utf-8 -*-
import logging

def logBaseTest():
    #format
    # %(asctime)s       Human-readable time
    # %(created)f       Time when the LogRecord was created (as returned by time.time()).
    # %(filename)should Filename portion of pathname.
    # %(funcName)s      Name of function containing the logging call.
    # %(levelname)s     Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
    # %(levelno)s       Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    # %(lineno)d        Source line number where the logging call
    # %(module)s        Module (name portion of filename).
    # %(msecs)d         Millisecond portion of the time when the LogRecord was created.
    # %(message)s
    # %(name)s          Name of the logger used to log the call.
    # %(pathname)s      Full pathname of the source file where the logging call was issued (if available).
    # %(process)d       Process ID (if available).
    # %(processName)s   Process name (if available).
    # %(relativeCreated)d   Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
    # %(thread)d        Thread ID (if available).
    # %(threadName)s    Thread name (if available).
    # 2016-06-16 16:12:16,830 , 1466064736.830909 , logTest.py , logBaseTest , DEBUG , 10 , 25 , logTest , 830 , This message should go to the log file , root , logTest.py , 2260 , MainProcess , 0 , 139922363930368 , MainThread
    logging.basicConfig(format='%(asctime)s , %(created)f , %(filename)s , %(funcName)s , %(levelname)s , %(levelno)s , %(lineno)d , %(module)s , %(msecs)d , %(message)s , %(name)s , %(pathname)s , %(process)d , %(processName)s , %(relativeCreated)d , %(thread)d , %(threadName)s' ,\
                        datefmt='%m/%d/%Y %I:%M:%S %p' ,\
                        filename='example.log', \
                        level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

    #set variable data
    logging.warning('%s before you %s', 'Look', 'leap!')

def logAdvancedTest():
    # create logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch2 = logging.FileHandler('advanced.log')
    ch2.setLevel(logging.WARNING)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    ch2.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(ch2)

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')


def logAdvanced2Test():
    import logging.config
    from datetime import datetime , timedelta , date
    # from logging.handlers import TimedRotatingFileHandler

    #在定義檔中設定
    logging.config.fileConfig('logging.conf')

    # create logger
    # 從定義檔中指定
    logger = logging.getLogger('log2')

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == "__main__":
    # logBaseTest()
    # logAdvancedTest()
    logAdvanced2Test()