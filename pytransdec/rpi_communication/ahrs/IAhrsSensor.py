import abc


class IAhrsSensor(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def send_data(self, data):
		pass
		
	@abc.abstractmethod
	def log(self, msg, logtype):
		pass
