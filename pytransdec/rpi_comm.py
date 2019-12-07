from rpi_communication.depth.depth import DepthSensor
from rpi_communication.definitions import DEFLOG
from rpi_communication.ports import DEPTH_DRIVER_PORT

depth = DepthSensor(DEPTH_DRIVER_PORT, DEFLOG.DEPTH_LOCAL_LOG, 'depth', DEFLOG.LOG_DIRECTORY) 
while True:
	depth.sendDepth(1)