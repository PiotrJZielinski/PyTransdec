import time

from rpi_communication.engine.IEngineSlave import IEngineSlave
from rpi_communication.base_communication import BaseCommunication

class EngineSlave(BaseCommunication, IEngineSlave):
    def __init__(self, port, is_log, log_file_name, log_directory):
        super(EngineSlave, self).__init__(port, is_log, log_file_name, log_directory)

    def get_movements(self):
        return self.client.get_data()

    def log(self, msg, logtype='info'):
        if self.logger:
            self.logger.log(msg, logtype=logtype)

