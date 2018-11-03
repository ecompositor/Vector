#!/usr/bin/env python3

import anki_vector
import time
from anki_vector.util import degrees, distance_mm, speed_mmps


def main():
    args = anki_vector.util.parse_command_args()

    # Connect to Vector
    with anki_vector.Robot(args.serial, request_control = True, enable_camera_feed = True, show_viewer = True) as robot:
        # Drive off charger and then release control
        robot.behavior.drive_off_charger()
        robot.release_control()

        # Now watch vector through the viewer as he does his thing...

        try:
            # Wait indefinitely
            while True: time.sleep(1)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
