import abc


class IBallGrapperActivator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_ball_grapper_data(self):
        pass

    @abc.abstractmethod
    def log(self, msg, logtype):
    	pass
