import time

from rpi_communication.ahrs.IAhrsSensor import IAhrsSensor
from rpi_communication.base_communication import BaseCommunication
from rpi_communication.definitions import RPI_COMM_DICT
from typing import Dict, List, Tuple, Union

class AhrsSensor(BaseCommunication, IAhrsSensor):
	def __init__(self, port, is_log, log_file_name, log_directory):
		super(AhrsSensor, self).__init__(port, is_log, log_file_name, log_directory)

	def send_data(self, data: Dict):
		print(data)
		self.client.send_data(data)

	def log(self, msg, logtype='info'):
		if self.logger:
			self.logger.log(msg, logtype=logtype)

if __name__ == '__main__':
	depth_sensor = AhrsSensor()
	while True:
		depth_sensor.send_acceleration(0,0,0)
