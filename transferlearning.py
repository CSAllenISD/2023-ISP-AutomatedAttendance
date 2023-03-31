import numpy as np
import cv2
import keras
from keras.applications.resnet50 import ResNet50
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential
from sklearn.metrics import accuracy_score

def compare_facial_recognition_models():
    # Load the ResNet50-based model
    model_resnet50 = keras.models.load_model('facial_recognition_model.h5')

    # Define the CNN model
    num_classes = 2
    model_cnn = Sequential()
    model_cnn.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
    model_cnn.add(MaxPooling2D((2, 2)))
    model_cnn.add(Conv2D(64, (3, 3), activation='relu'))
    model_cnn.add(MaxPooling2D((2, 2)))
    model_cnn.add(Conv2D(128, (3, 3), activation='relu'))
    model_cnn.add(MaxPooling2D((2, 2)))
    model_cnn.add(Conv2D(128, (3, 3), activation='relu'))
    model_cnn.add(MaxPooling2D((2, 2)))
    model_cnn.add(Flatten())
    model_cnn.add(Dense(512, activation='relu'))
    model_cnn.add(Dense(num_classes, activation='softmax'))
    model_cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Load the dataset
    train_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
            'train',
            target_size=(224, 224),
            batch_size=32,
            class_mode='categorical')

    # Train the ResNet50-based model
    model_resnet50.fit_generator(
            train_generator,
            steps_per_epoch=100,
            epochs=10,
            verbose=0)

    # Train the CNN model
    model_cnn.fit_generator(
            train_generator,
            steps_per_epoch=100,
            epochs=10,
            verbose=0)

    # Test the models on a sample of data
    sample_datagen = ImageDataGenerator(rescale=1./255)
    sample_generator = sample_datagen.flow_from_directory(
            'sample',
            target_size=(224, 224),
            batch_size=32,
            class_mode='categorical')

    y_true = []
    y_pred_resnet50 = []
    y_pred_cnn = []

    for i in range(len(sample_generator)):
        x, y = sample_generator[i]
        y_true.extend(np.argmax(y, axis=1))
        y_pred_resnet50.extend(np.argmax(model_resnet50.predict(x), axis=1))
        y_pred_cnn.extend(np.argmax(model_cnn.predict(x), axis=1))

    # Calculate and print the accuracies
    acc_resnet50 = accuracy_score(y_true, y_pred_resnet50)
    acc_cnn = accuracy_score(y_true, y_pred_cnn)
    print('ResNet50 accuracy: {:.2f}%'.format(acc_resnet50 * 100))
    print('CNN accuracy: {:.2f}%'.format(acc_cnn * 100))