# import the necessary packages
from __future__ import print_function
from CamVideoStream import CamVideoStream
from fps import FPS
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-src", "--source", type=str, default=0,
	help="Camera IP")
ap.add_argument("-d", "--display", type=int, default=True,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args()) 

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = CamVideoStream(args["source"]).start()
fps = FPS().start()

# loop over some frames...this time using the threaded stream
while vs.open():
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = cv2.resize(frame, (800, 450), interpolation=cv2.INTER_LINEAR)
 
	# check to see if the frame should be displayed to our screen
	if args["display"]:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
 
	# update the FPS counter
	fps.update()
 
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()