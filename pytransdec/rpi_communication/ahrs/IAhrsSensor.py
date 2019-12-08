import abc


class IAhrsSensor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
	def send_acceleration(self, acceleration_x, acceleration_y, acceleration_z):
        pass
		
    @abc.abstractmethod
	def send_angular_acceleration(self, acceleration_x, acceleration_y, acceleration_z):
		pass
    @abc.abstractmethod
    def log(self, msg, logtype):
    	pass
