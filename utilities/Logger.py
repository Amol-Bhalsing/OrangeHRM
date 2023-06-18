import logging
import inspect


class LogGen:
    @staticmethod
    def loggen():
        classname=inspect.stack()[1][3]
        logger=logging.getLogger(classname)
        file=logging.FileHandler(r'D:\SoftwareTesting\Automation Testing\Framework_Projects\OrangeHRM\Logs\logfile.log')
        format=logging.Formatter("%(asctime)s :  %(levelname)s : %(name)s : %(funcName)s: %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger

'''
# Levels of logger
1.DEBUG
2.INFO
3.WARN
4.ERROR 
5.CRITICAL

'''
