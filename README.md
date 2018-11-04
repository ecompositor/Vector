# Vector
Anki Vector Robot SDK Experiments.

## Connect to Vector without stopping normal behaviors

This project contains a patch to the Vector SDK that will allow you to connect to Vector without stopping his normal behaviors.  It also allows you take control and release control as needed.

### Applying the patch
Download the `apply_patch.py` file from this project.  The options for the tool are listed below: 

```txt
Anki Vector SDK patch tool

This tool patches the SDK package to include additional functionality.

Usage: apply_patch.py [options]

Options:
  -h, --help                show this help message and exit
  -q, --quiet               print only warnings and errors
  -v, --verbose             be verbose
  --debug                   debug mode
  --diffstat                print diffstat and exit
  -d DIR, --directory=DIR   specify root directory for applying patch
  --revert                  apply patch in reverse order (unpatch)
```

Run the tool with Python to automatically find the location of the Python module and patch it:

```txt
> python apply_patch.py
```

And the result should look something like this:

```txt
Anki Vector SDK patch tool

This tool patches the SDK package to include additional functionality.

Patching the Path: C:\Bin\Python37\lib\site-packages\anki_vector

Done.
```

### Using the new options

Connect to Vector without taking control:
```python
# Connect to Vector without taking control
with anki_vector.Robot(args.serial, request_control = False) as robot:
```

Grab control of Vector before trying to move him:

```python
# Request control
robot.conn.request_control()
# Wait for control to be granted before continuing
robot.conn.control_granted_event.wait()
```

Release control when you are done with him:

```python
# Release control vector
robot.release_control()
```

### Example Projects

Patch examples are stored in the `examples` folder:

#### video.py
Watch Vector through the viewer as he does his normal stuff.

#### workout.py
Vector will start doing his workout when he sees his cube.  Grab the cube, tell Vector to "Go exploring" and then place the cube in front of him for the best effect.  Vector will only do the workout once per script execution.

[Video](https://www.youtube.com/watch?v=GCCpfzEIx44)

#### events.py
Prints all the details of all the events that Vector generates.  Useful for learning.

#### anim_list.py
Saves all of Vector's animations to anim.txt

### Notes

* Some operations on Vector, like saying text, does not require you to take control.  
* If you have not taken control and try an issue a movement command, your script will stop working.


