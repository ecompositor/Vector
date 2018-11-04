#!/usr/bin/env python3

import anki_vector
import time
import functools
import time
from threading import Event

from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.events import Events

def main():
    args = anki_vector.util.parse_command_args()

    # The robot drives straight, stops and then turns around
    with anki_vector.Robot(args.serial, request_control = False, default_logging=False) as robot:
        
        anim_names = robot.anim.anim_list
        anim_names.sort()
        with open("anim.txt", 'w') as file_handler:
            for item in anim_names:
                file_handler.write("{}\n".format(item))

if __name__ == "__main__":
    main()
