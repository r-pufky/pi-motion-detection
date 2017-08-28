# pi-motion-detection
Detect motion using Raspberry Pi Camera.

Install Instructions
--------------------
1. Login raspberry pi, install dependencies and clone code

```bash
sudo apt install python-picamera python3-picamera python-picamera-docs
git clone https://github.com/r-pufky/pi-motion-detection
```

2. [Ensure camera port is enabled](https://www.raspberrypi.org/documentation/configuration/camera.md)
* Select Camera -> Enable
```bash
sudo raspi-config
```

Usage:
------
This just provides a convient way to detect motion; you'll need to handle polling yourself. You
should probably throttle DetectMotion() as it does not explicitly delay when called.

```python
import pi_motion_detection

detector = pi_motion_detection.PiMotionDetection()
while true:
  if detector.DetectMotion():
    TakeSomeActionHere()
```

Detection Settings
------------------
You can setup detection settings using the class. Just read the docstrings.

```python
import pi_motion_detection
detector = pi_motion_detection.PiMotionDetection()

detector.DETECT_THRESHOLD = 20
detector.DETECT_SENSITIVITY = 200
detector.DETECT_WIDTH = 1024
detector.DETECT_HEIGHT = 768
```
