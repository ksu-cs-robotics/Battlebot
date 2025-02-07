#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
import rospkg
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# import face_recognition

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image, queue_size=10)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image_raw",Image,self.callback)
    self.face_locations = []

    rospack = rospkg.RosPack()
    self.cascPath = rospack.get_path('solution') + "/scripts/example/haarcascade_frontalface_default.xml"
    self.faceCascade = cv2.CascadeClassifier(self.cascPath)

  def callback(self,data):
    try:
      frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    #-----------SIMPLE DRAWING ON IMAGE-----------------
    # (rows,cols,channels) = frame.shape
    # if cols > 60 and rows > 60 :
    #   cv2.circle(frame, (50,50), 10, 255)
    #-----------SIMPLE DRAWING ON IMAGE-----------------

    #-----------------------USING FACE_RECOGNITION LIBRARY----------------------------------------
    # # Resize frame of video to 1/4 size for faster face detection processing
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # # Find all the faces and face encodings in the current frame of video
    # self.face_locations = face_recognition.face_locations(small_frame, model="cnn")

    # # Display the results
    # for top, right, bottom, left in self.face_locations:
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4

    #     # Extract the region of the image that contains the face
    #     face_image = frame[top:bottom, left:right]

    #     # Blur the face image
    #     face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

    #     # Put the blurred face region back into the frame image
    #     frame[top:bottom, left:right] = face_image
    #-----------------------USING FACE_RECOGNITION LIBRARY----------------------------------------

    #------------------------USE Cascades-------------------------------------------------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = self.faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #------------------------USE Cascades-------------------------------------------------

    cv2.imshow("Image window", frame)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)