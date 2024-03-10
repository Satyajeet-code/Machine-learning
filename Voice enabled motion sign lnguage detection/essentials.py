
import cv2 
import sklearn
import numpy 
import os 
import mediapipe

holistic_model = mediapipe.solutions.holistic
draw_model = mediapipe.solutions.drawing_utils 

def get_feed(image, calc):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    image.flags.writeable = False                   
    output = calc.process(image)      
    image.flags.writeable = True                
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, output

def get_dots(image, output):
    draw_model.draw_landmarks(image, output.face_landmarks, holistic_model.FACEMESH_TESSELATION) 
    draw_model.draw_landmarks(image, output.pose_landmarks, holistic_model.POSE_CONNECTIONS) 
    draw_model.draw_landmarks(image, output.left_hand_landmarks, holistic_model.HAND_CONNECTIONS)
    draw_model.draw_landmarks(image, output.right_hand_landmarks, holistic_model.HAND_CONNECTIONS)

def get_dot(out):
    shoulder = numpy.array([[i.x, i.y, i.z, i.visibility] for i in out.pose_landmarks.landmark]).flatten() if out.pose_landmarks else numpy.zeros(33*4)
    face_shape = numpy.array([[i.x, i.y, i.z] for i in out.face_landmarks.landmark]).flatten() if out.face_landmarks else numpy.zeros(468*3)
    left_hand = numpy.array([[i.x, i.y, i.z] for i in out.left_hand_landmarks.landmark]).flatten() if out.left_hand_landmarks else numpy.zeros(21*3)
    right_hand = numpy.array([[i.x, i.y, i.z] for i in out.right_hand_landmarks.landmark]).flatten() if out.right_hand_landmarks else numpy.zeros(21*3)
    return numpy.concatenate([shoulder, face_shape, left_hand, right_hand])