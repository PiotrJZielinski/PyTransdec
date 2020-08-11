from typing import Dict, List, Tuple, Union

OBSERVATIONS = {
				'a_x': 'acceleration_x',
				'a_y': 'acceleration_y',
				'a_z': 'acceleration_z',
				'eps_x': 'angular_acceleration_x',
				'eps_y': 'angular_acceleration_y',
				'eps_z': 'angular_acceleration_z',
				'phi_x': 'rotation_x',
				'phi_y': 'rotation_y',
				'phi_z': 'rotation_z',
				'd': 'depth',
				'x': 'bounding_box_x',
				'y': 'bounding_box_y',
				'w': 'bounding_box_w',
				'h': 'bounding_box_h',
				'p': 'bounding_box_p',
				'relative_x': 'relative_x',
				'relative_y': 'relative_y',
				'relative_z': 'relative_z',
				'relative_yaw': 'relative_yaw',
				'grab_state': 'grab_state',
				'is_torpedo_hit': 'is_torpedo_hit',
				'torpedo_ready': 'torpedo_ready',
				'front_distance': 'front_distance',
				'hydrophone_angle': 'hydrophone_angle'
}

CAMERAS = {
				'front': 0,
				'bottom': 1
}

RESET_KEYS = ['CollectData', 'EnableNoise', 'Positive', 'AgentMaxSteps', 'FocusedObject', 'EnableBackgroundImage', 'ForceToSaveAsNegative']