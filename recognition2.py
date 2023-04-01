import cv2
import face_recognition
'''
# image comparison

img = cv2.imread("faces/Cameron Farley.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("faces/Oliver Hankins.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

img3 = cv2.imread("faces/photo-1507003211169-0a1dd7228f2d.jpg")
rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

#test comparison
result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)

cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)
'''

# encodes faces from a faces folder
sfr = SimpleFacerec()
sfr.load_encoding_images("faces/")

cap = cv2.VideoCapture(2)

while True:
  ret, frame = cap.read()
  
  # face detection
  face_locations, face_names = sfr.detect_known_faces(frame)
  for face_loc, name in zip(face_locations, face_names):
    # debugging 
    # print(face_loc)
    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    
    cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    
  cv2.imshow("Frame", frame)
  
  key = cv2.waitKey(1)
  if key == 27:
    break
  
cap.release()
cv2.destroyAllWindows()
