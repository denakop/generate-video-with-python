import cv2
from PIL import Image
import os


class GenerateVideo:
    def __init__(self, video_name):
        self.video_name = video_name
        self.generate_video()

    def generate_video(self):
        image_folder = 'assets/images/'
        video_name = self.video_name + '.avi'

        each_image_duration = 5  # in secs
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # define the video codec

        images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, fourcc, 1.0, (width, height))

        for image in images:
            for _ in range(each_image_duration):
                video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
        self.remove_images()

    @staticmethod
    def remove_images():
        image_folder = 'assets/images/'
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
        for image in images:
            os.remove(os.path.join(image_folder, image))
