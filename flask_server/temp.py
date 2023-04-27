obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    William_face_encoding,
    obama_face_encoding
]
known_face_names = [
    "William Clymire",
    "Barak Obama"
]