#!/usr/bin/python
#
# PiMotionDetection detects 'motion' using the picamera library. This simply
# determines if the image has changed, allowing the consumer of this class
# to take further actions. This should be polled.

# Usage:
#   detector = pi_motion_detection.PiMotionDetection()
#   while true:
#     if detector.DetectMotion():
#       TakeSomeActionHere()
#     time.sleep(5)
#
import picamera
import picamera.array


class PiMotionDetection(object):
  """ Detects motion using Pi Camera.

  Attributes:
    DETECT_THRESHOLD: Integer difference for specific pixel to detect a
        'changed' pixel. Default 10.
    DETECT_SENSITIVITY: Integer number of 'changed' pixels to trigger a
        motion detection. Default 100.
    DETECT_WIDTH: Integer width of image used to test for motion. Default 128.
    DETECT_HEIGHT: Integer height of image used to test for motion. Default 80.
  """	  
  DETECT_THRESHOLD = 10
  DETECT_SENSITIVITY = 100
  DETECT_WIDTH = 128
  DETECT_HEIGHT = 80

  def __init__(self):
    """ Initalize PiMotionDetector."""
    self._source_image = None
    self._diff_image = None
    self._source_image = self._DetectCapture()

  def _DetectCapture(self):
    """ Capture an image to be used for detection.

    Returns:
      stream object containing capturing image data.
    """
    with picamera.PiCamera() as camera:
      camera.resolution = (self.DETECT_WIDTH, self.DETECT_HEIGHT)
        with picamera.array.PiRGBArray(camera) as stream:
          camera.exposure_mode = 'auto'
          camera.awb_mode = 'auto' 
          camera.capture(stream, format='rgb')
          return stream.array

def DetectMotion(self):
  """ Determine if there is motion between two images.

  Returns:
    Boolean True if motion is 'detected'.
  """
  self._diff_image = self._DetectCapture()
  diff_count = 0
  for column in range(0, self.DETECT_WIDTH):
    for row in range(0, self.DETECT_HEIGHT):
      if (abs(int(self._source_image[row][column][1]) -
          int(self._diff_image[row][column][1]))
          > self.DETECT_THRESHOLD):
        diff_count += 1
  self._source_image = self._diff_image
  return diff_count > self.DETECT_SENSITIVITY

            
if __name__ == '__main__':
  pass
