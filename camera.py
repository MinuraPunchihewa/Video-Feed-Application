import cv2


class VideoCamera(object):
    def __init__(self, filename):
        self.video = cv2.VideoCapture(filename)

    def __del__(self):
        self.video.release()

    # initialize a static variable to store the frame number
    frame_num = 0

    def get_frame(self):
        while self.video.isOpened():
            video_ret, frame = self.video.read()

            # use our model to detect the number of vehicles

            if video_ret:
                self.frame_num += 1

                img_ret, jpeg = cv2.imencode('.jpg', frame)
                return jpeg.tobytes(), self.frame_num


