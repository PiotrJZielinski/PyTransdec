import time

from rpi_communication.torpedo.ITorpedoController import ITorpedoController
from rpi_communication.base_communication import BaseCommunication

class TorpedoActivator(BaseCommunication, ITorpedoController):
    def __init__(self, port, is_log, log_file_name, log_directory):
        super(TorpedoActivator, self).__init__(port, is_log, log_file_name, log_directory)

    def get_torpedo_data(self):
        self.client.get_data()

    def log(self, msg, logtype='info'):
        if self.logger:
            self.logger.log(msg, logtype=logtype)

if __name__ == '__main__':
    torpedo_activator = TorpedoActivator()
    while True:
        torpedo_activator.get_torpedo_data()
