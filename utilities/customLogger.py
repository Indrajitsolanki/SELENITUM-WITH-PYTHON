import logging

import pytest


class LogGen:
    @staticmethod
    def Loggen():
        logging.basicConfig(filename=".\\logs\\autamation.log",
                            format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S' )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



