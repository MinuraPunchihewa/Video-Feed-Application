import cv2


class VideoCamera(object):
    def __init__(self, filename):
        self.video = cv2.VideoCapture(filename)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        while self.video.isOpened():
            ret, frame = self.video.read()

            # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

            ret, jpeg = cv2.imencode('.jpg', frame)

            return jpeg.tobytes()


