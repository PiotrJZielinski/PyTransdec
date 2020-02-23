class DEFLOG:
    LOG_DIRECTORY = "logs/"

    DEPTH_LOCAL_LOG = True

    AHRS_LOCAL_LOG = True

    HYDROPHONES_LOCAL_LOG = False

    DISTANCE_LOCAL_LOG = True

    MOVEMENTS_LOCAL_LOG = True
    MANIPULATOR_LOCAL_LOG = False
    TORPEDOES_LOCAL_LOG = False
    BALL_GRAPPER_LOCAL_LOG = False


RPI_COMM_DICT = {
				'acceleration_x': 'lineA_x',
				'acceleration_y': 'lineA_y',
				'acceleration_z': 'lineA_z',
				'angular_acceleration_x' : 'angularA_x',
				'angular_acceleration_y' : 'angularA_y',
				'angular_acceleration_z' : 'angularA_z',
				'rotation_x' : 'roll',
				'rotation_y' : 'pitch',
				'rotation_z' : 'yaw'
}
