import abc


class IEngineSlave(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_movements(self):
        pass

    @abc.abstractmethod
    def log(self, msg, logtype):
    	pass
