from src import vehicle as vehicle_module
from src import distance_sensor as distance_sensor_module
import time
import cv2

if __name__ == '__main__':
     
	
    distance_sensor1 = distance_sensor_module.DistanceSensor({
	    "pins": {
		    "echo": 23,
		    "trigger": 24
	    }
    })

    distance_sensor2 = distance_sensor_module.DistanceSensor({
		"pins": {
			"echo": 17,
			"trigger": 27
		}
	})
	
    vehicle = vehicle_module.Vehicle(
        {
            "motors": {
                "left": {
                    "pins": {
                        "speed": 13,
                        "control1": 5,
                        "control2": 6
                    }
                },
                "right": {
                    "pins": {
                        "speed": 12,
                        "control1": 7,
                        "control2": 8
                    }
                }
            }
        }
    )
    while True:
        
        if distance_sensor1.distance == 1:
            if distance_sensor2.distance >= 0.30 and distance_sensor2.distance <= 0.95:
                print('In Forward')
                vehicle.drive_forward(1)
            
            if distance_sensor2.distance >= 0.95:
                print('In Left')
                vehicle.pivot_right(1)

        else:
            if distance_sensor2.distance >= 0.30 and distance_sensor2.distance <= 0.95:
                print('Out Left')
                vehicle.pivot_left(1)
            
            elif distance_sensor2.distance >= 0.95:
                print('Right')
                vehicle.pivot_right(1)
                
		
        




