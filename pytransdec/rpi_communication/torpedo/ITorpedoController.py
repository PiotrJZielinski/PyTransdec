import abc


class IDepthSensor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send_depth(self, depth):
        pass

    @abc.abstractmethod
    def log(self, msg, logtype):
    	pass
