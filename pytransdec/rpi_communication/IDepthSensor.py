import abc


class IDepthSensor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sendDepth(self, depth):
        pass

    @abc.abstractmethod
    def log(self, msg, logtype):
    	pass
