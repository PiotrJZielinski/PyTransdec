import time

from rpi_communication.ball_grapper.IBallGrapperActivator import IBallGrapperActivator
from rpi_communication.base_communication import BaseCommunication

class BallGrapperActivator(BaseCommunication, IBallGrapperActivator):
    def __init__(self, port, is_log, log_file_name, log_directory):
        super(BallGrapperActivator, self).__init__(port, is_log, log_file_name, log_directory)

    def get_ball_grapper_data(self):
        self.client.get_data()

    def log(self, msg, logtype='info'):
        if self.logger:
            self.logger.log(msg, logtype=logtype)

if __name__ == '__main__':
    ball_grapper_activator = BallGrapperActivator()
    while True:
        ball_grapper_activator.get_ball_grapper_data()
