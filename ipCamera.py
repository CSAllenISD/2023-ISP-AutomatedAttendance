from flask import Flask, render_template, Response
import cv2

#Flask App
app = Flask(__name__)

camera = rtsp://admin:placeholderIPforCam/cam/realmonitor?channel=1&subtype=0

# frame for frame read for camera to livestream

def gen_frames():
        while True:
            success, frame = camera.read()  
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



                @app.route('/')
                def index():
                        return render_template('ipCamera.html')

                @app.route('/video_feed')
                def video_feed():
                    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

            if __name__ == '__main__':
                        app.run(debug=True)
