#!/usr/bin/env python3

import anki_vector
import time
import functools
import time
from threading import Event

from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.events import Events

# Robot State Flags
NoneRobotStatusFlag     = 0
IS_MOVING               = 0x1
IS_CARRYING_BLOCK       = 0x2
IS_PICKING_OR_PLACING   = 0x4
IS_PICKED_UP            = 0x8
IS_BUTTON_PRESSED       = 0x10
IS_FALLING              = 0x20
IS_ANIMATING            = 0x40
IS_PATHING              = 0x80
LIFT_IN_POS             = 0x100
HEAD_IN_POS             = 0x200
CALM_POWER_MODE         = 0x400
IS_BATTERY_DISCONNECTED = 0x800
IS_ON_CHARGER           = 0x1000
IS_CHARGING             = 0x2000
CLIFF_DETECTED          = 0x4000
ARE_WHEELS_MOVING       = 0x8000
IS_BEING_HELD           = 0x10000
IS_MOTION_DETECTED      = 0x20000
IS_BATTERY_OVERHEATED   = 0x40000

def main():
    args = anki_vector.util.parse_command_args()

    def on_audio_send_mode_changed(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      

    def on_cube_connection_lost(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      

    def on_object_appeared(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print(f"obj: {event.obj}")
        print(f"image_rect: {event.image_rect}")
        print(f"pose: {event.pose}")       
        print()      

    def on_object_available(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      
        
    def on_object_disappeared(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print(f"obj: {event.obj}")
        print()      

    def on_object_finished_move(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print(f"obj: {event.obj}")
        print(f"move_duration: {event.move_duration}")
        print()      

    def on_object_moved(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      

    def on_object_observed(robot, event_type, event):
        print(f"Event: {event_type}")
        print(f"obj: {event.obj}")
        print(f"image_rect: {event.image_rect}")
        print(f"pose: {event.pose}")
        print(event)
        print()      

    def on_object_stopped_moving(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      

    def on_object_up_axis_changed(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()     

    def on_robot_observed_face(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      

    def on_robot_observed_object(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()     

    def on_robot_state(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        status = []
        if (event.status & IS_MOVING): status.append("IS_MOVING")
        if (event.status & IS_CARRYING_BLOCK): status.append("IS_CARRYING_BLOCK")
        if (event.status & IS_PICKING_OR_PLACING): status.append("IS_PICKING_OR_PLACING")
        if (event.status & IS_PICKED_UP): status.append("IS_PICKED_UP")
        if (event.status & IS_BUTTON_PRESSED): status.append("IS_BUTTON_PRESSED")
        if (event.status & IS_FALLING): status.append("IS_FALLING")
        if (event.status & LIFT_IN_POS): status.append("LIFT_IN_POS")
        if (event.status & HEAD_IN_POS): status.append("HEAD_IN_POS")
        if (event.status & CALM_POWER_MODE): status.append("CALM_POWER_MODE")
        if (event.status & IS_BATTERY_DISCONNECTED): status.append("IS_BATTERY_DISCONNECTED")
        if (event.status & IS_ON_CHARGER): status.append("IS_ON_CHARGER")
        if (event.status & CLIFF_DETECTED): status.append("CLIFF_DETECTED")
        if (event.status & ARE_WHEELS_MOVING): status.append("ARE_WHEELS_MOVING")
        if (event.status & IS_BEING_HELD): status.append("IS_BEING_HELD")
        if (event.status & IS_MOTION_DETECTED): status.append("IS_MOTION_DETECTED")
        if (event.status & IS_BATTERY_OVERHEATED): status.append("IS_BATTERY_OVERHEATED")
        print("Status: " + ", ".join(status))
        print()      

    def on_timestamped_status(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event);
        print()      

    def on_wake_word(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      

    def on_stimulation_info(robot, event_type, event):
        print(f"Event: {event_type}")
        print(event)
        print()      

    # Do not take control of Vector
    with anki_vector.Robot(args.serial, request_control = False, enable_camera_feed = False, show_viewer = False, default_logging=False) as robot:

        robot.faces.enable_vision_mode(1)

        on_audio_send_mode_changed = functools.partial(on_audio_send_mode_changed, robot)
        on_cube_connection_lost = functools.partial(on_cube_connection_lost, robot)
        on_object_appeared = functools.partial(on_object_appeared, robot)
        on_object_available = functools.partial(on_object_available, robot)
        on_object_disappeared = functools.partial(on_object_disappeared, robot)
        on_object_finished_move = functools.partial(on_object_finished_move, robot)
        on_object_moved = functools.partial(on_object_moved, robot)
        on_object_observed = functools.partial(on_object_observed, robot)
        on_object_stopped_moving  = functools.partial(on_object_stopped_moving, robot)
        on_object_up_axis_changed  = functools.partial(on_object_up_axis_changed , robot)
        on_robot_observed_face  = functools.partial(on_robot_observed_face, robot)
        on_robot_observed_object  = functools.partial(on_robot_observed_object , robot)
        on_robot_state = functools.partial(on_robot_state, robot)
        on_timestamped_status = functools.partial(on_timestamped_status, robot)
        on_wake_word = functools.partial(on_wake_word, robot)
        on_stimulation_info = functools.partial(on_stimulation_info, robot)

        robot.events.subscribe(on_audio_send_mode_changed, Events.audio_send_mode_changed)
        robot.events.subscribe(on_cube_connection_lost, Events.cube_connection_lost)
        robot.events.subscribe(on_object_appeared, Events.object_appeared)
        robot.events.subscribe(on_object_available, Events.object_available)
        robot.events.subscribe(on_object_disappeared, Events.object_disappeared)
        robot.events.subscribe(on_object_finished_move, Events.object_finished_move)
        robot.events.subscribe(on_object_moved, Events.object_moved)
        robot.events.subscribe(on_object_observed, Events.object_observed)
        robot.events.subscribe(on_object_stopped_moving, Events.object_stopped_moving)
        robot.events.subscribe(on_object_up_axis_changed, Events.object_up_axis_changed)
        robot.events.subscribe(on_robot_observed_face, Events.robot_observed_face)
        robot.events.subscribe(on_robot_observed_object, Events.robot_observed_object)
        # Uncomment to add robot state event -- but generates a lot of output
        #robot.events.subscribe(on_robot_state, Events.robot_state)
        robot.events.subscribe_by_name(on_timestamped_status, "time_stamped_status")
        robot.events.subscribe_by_name(on_wake_word, "wake_word")
        robot.events.subscribe_by_name(on_stimulation_info, "stimulation_info")

        try:
            # Wait indefinitely
            while True: 
                time.sleep(1)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
