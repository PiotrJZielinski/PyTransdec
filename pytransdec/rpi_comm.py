from rpi_communication.depth.depth import DepthSensor
from rpi_communication.engine.engine import EngineSlave
from rpi_communication.ahrs.ahrs import AhrsSensor
from rpi_communication.definitions import DEFLOG
from rpi_communication.ports import DEPTH_DRIVER_PORT, ENGINE_SLAVE_PORT, AHRS_DRIVER_PORT



engine = EngineSlave(ENGINE_SLAVE_PORT, DEFLOG.MOVEMENTS_LOCAL_LOG, 'movement', DEFLOG.LOG_DIRECTORY) 
while True:
	print("Message: {0}".format(engine.get_movements()))

class RPi_Communication:
	def __init__(self):
		log_directory = DEFLOG.LOG_DIRECTORY
		self.engine = EngineSlave(ENGINE_SLAVE_PORT, DEFLOG.MOVEMENTS_LOCAL_LOG, 'movement', log_directory)
		self.depth_sensor = DepthSensor(DEPTH_DRIVER_PORT, DEFLOG.DEPTH_LOCAL_LOG, 'depth', log_directory)
		self.ahrs = AhrsSensor(AHRS_DRIVER_PORT, DEFLOG.AHRS_LOCAL_LOG, 'ahrs', log_directory)


	def send_to_rpi(self, data: Dict):
		self.depth_sensor.send_depth(data['depth'])
		self.ahrs.send_acceleration(data['acceleration_x'], data['acceleration_y'], data['acceleration_z'])
		self.ahrs.send_acceleration(data['angular_acceleration_x'], data['angular_acceleration_y'], data['angular_acceleration_z'])

	def get_movements(self):
		return self.engine.get_movements()