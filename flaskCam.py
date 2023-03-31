camera = cv2.VideoCapture(0)

'''
for ip camera use -
rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp'

for local webcam use cv2.VideoCapture(0)
'''


# Adding window and generating frames from the camera

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

'''
defining app route for default page of the web-app

@app.route('/')
def index():
  return render_template('index.html')
'''

'''
defining app route for video feed

@app.route('/video_feed')
def video_feed():
  return response(gen_frames(), mimtype='multipart/x-mixed-replace; boundary=frame')
'''

