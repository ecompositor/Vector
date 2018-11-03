#!/usr/bin/env python3

import anki_vector
import time
import functools
import time
from threading import Event

from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.events import Events

class VectorState(object):
    pass

# Global state for Vector
vector_state = VectorState()
# Should vector start his workout?
vector_state.start_workout = True
# Did vector finish his workout?
vector_state.workout_done = False

def do_workout(robot):
    # Aquire control
    robot.conn.request_control()
    robot.conn.control_granted_event.wait()

    # If necessary, Move Vector's Head and Lift down
    robot.behavior.set_head_angle(degrees(-5.0))
    robot.behavior.set_lift_height(0.0)

    # connect the cube
    robot.world.connect_cube()

    # If connected to cube do the workout
    if robot.world.connected_light_cube:
        print("Begin cube docking...")
        # TODO Try with num_retries of 3
        dock_response = robot.behavior.dock_with_cube(robot.world.connected_light_cube, num_retries=3)
        docking_result = dock_response.result

        if docking_result.code != anki_vector.messaging.protocol.ActionResult.ACTION_RESULT_SUCCESS:
            print("Cube docking failed with code {0} ({1})".format(str(docking_result).rstrip('\n\r'), docking_result.code))
        else:
            # Have Vector Lift his Cube 5 times
            robot.behavior.set_lift_height(100.0)
            robot.say_text("One")          
            robot.behavior.set_lift_height(20.0, duration=0.5)

            robot.behavior.set_lift_height(100.0)
            robot.say_text("Two")
            robot.behavior.set_lift_height(20.0, duration=0.5)
            
            robot.behavior.set_lift_height(100.0,duration=0.75)
            robot.say_text("Three")
            robot.behavior.set_lift_height(20.0, duration=0.5)
            
            robot.behavior.set_lift_height(100.0,duration=1.0)
            robot.say_text("Four")
            robot.behavior.set_lift_height(20.0, duration=0.5)

            robot.behavior.set_lift_height(100.0,duration=1.5)
            robot.say_text("Five")
            robot.behavior.set_lift_height(0.0, duration=0.5)       

            # Vector completed his workout
            vector_state.workout_done = True

    robot.world.disconnect_cube()    
    robot.release_control()

def main():
    args = anki_vector.util.parse_command_args()

    def on_robot_observed_object(robot, event_type, event):
        # Did Vector see his light cube?
        # Has he done his workout?
        # If not, do the workout now.
        if event.object_type == anki_vector.objects.LIGHT_CUBE_1_TYPE:
            # Vector should start his workout
            vector_state.start_workout = True

    # Start the connection with the robot but do not request control
    with anki_vector.Robot(args.serial, request_control = False, default_logging=False) as robot:

        # Subscribe to the on_robot_observed_object event
        on_robot_observed_object = functools.partial(on_robot_observed_object, robot)
        robot.events.subscribe(on_robot_observed_object, Events.robot_observed_object)

        try:
            # Wait indefinitely
            while True: 
                # Sleep for one second
                time.sleep(1)
                # Check if vector should start workout 
                if (vector_state.start_workout and not vector_state.workout_done):
                    do_workout(robot)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
