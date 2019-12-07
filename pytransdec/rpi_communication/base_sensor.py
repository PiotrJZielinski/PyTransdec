"""
Module includes BaseSensor class
"""
import zmq
import ast
import abc
from logpy import Logger

from rpi_communication.definitions import DEFLOG
from rpi_communication.rov_comm import Client


class BaseSensor(metaclass=abc.ABCMeta):
    """
    All sensors in sensors directory shoud inherit after this class
    """
    def __init__(self, port, is_log, log_file_name, log_directory):
        self.client = Client(port)
        self.logger = is_log
        if is_log:
            self.logger = Logger(filename=log_file_name, directory=log_directory)

    def __del__(self):
        if self.logger:
            self.logger.exit()

