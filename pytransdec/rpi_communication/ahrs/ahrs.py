import time

from rpi_communication.ahrs.IAhrsSensor import IAhrsSensor
from rpi_communication.base_communication import BaseCommunication

class AhrsSensor(BaseCommunication, IAhrsSensor):
    def __init__(self, port, is_log, log_file_name, log_directory):
        super(AhrsSensor, self).__init__(port, is_log, log_file_name, log_directory)

    def send_acceleration(self, acceleration_x, acceleration_y, acceleration_z):
        pass

	def send_angular_acceleration(self, acceleration_x, acceleration_y, acceleration_z):
		pass

    def log(self, msg, logtype='info'):
        if self.logger:
            self.logger.log(msg, logtype=logtype)

if __name__ == '__main__':
    depth_sensor = AhrsSensor()
    while True:
        self.client.send_data(depth)
