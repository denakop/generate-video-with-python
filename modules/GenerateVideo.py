import cv2
from PIL import Image
import os

class GenerateVideo:
    def __init__(self):
        self.generate_video()

    def generate_video(self):
        imageFolder = 'assets/images/'
        videoName = 'portalcretinos.avi'


        each_image_duration = 5  # in secs
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # define the video codec

        images = [img for img in os.listdir(imageFolder) if img.endswith(".png")]
        frame = cv2.imread(os.path.join(imageFolder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(videoName, fourcc, 1.0, (width, height))

        for image in images:
            for _ in range(each_image_duration):
                video.write(cv2.imread(os.path.join(imageFolder, image)))

        cv2.destroyAllWindows()
        video.release()

