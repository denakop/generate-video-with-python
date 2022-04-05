import cv2
import os


class GenerateVideo:
    def __init__(self, video_name, account_id):
        self.account_id = account_id
        self.video_name = video_name
        self.generate_video()

    def generate_video(self):
        if os.path.isdir('video/' + self.account_id) is False:
            os.mkdir('video/' + self.account_id)

        image_folder = 'assets/images/' + self.video_name
        video_name = 'video/' + self.account_id + '/' + self.video_name + '.mp4'

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


    def remove_images(self):
        image_folder = 'assets/images/' + self.video_name
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
        for image in images:
            os.remove(os.path.join(image_folder, image))
