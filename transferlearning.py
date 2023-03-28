import numpy as np
import cv2
import keras
from keras.applications.resnet50 import ResNet50
from keras.layers import Flatten, Dense
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator

# Step 1: Install the necessary libraries
# pip install tensorflow
# pip install keras
# pip install opencv-python

# Step 2: Load a pre-trained model
model = ResNet50(weights='imagenet', include_top=False)

# Step 3: Add new layers to the model
num_classes = 2 # Change this to the number of classes in your dataset
x = model.output
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

# Step 4: Freeze the pre-trained layers
for layer in model.layers:
    layer.trainable = False

# Step 5: Compile the model
new_model = Model(inputs=model.input, outputs=predictions)
new_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 6: Load the dataset
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        'train',
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical')

# Step 7: Train the model
new_model.fit_generator(
        train_generator,
        steps_per_epoch=100,
        epochs=10)

# Step 8: Save the model
new_model.save('facial_recognition_model.h5')

# Step 9: Use the model to recognize faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = keras.models.load_model('facial_recognition_model.h5')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (224, 224))
        roi_gray = np.reshape(roi_gray, (1, 224, 224, 1))
        prediction = model.predict(roi_gray)
        if np.argmax(prediction) == 0:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame, 'John Doe', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        else:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame, 'Jane Doe', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Facial Recognition AI', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
