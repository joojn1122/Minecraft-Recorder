import cv2
import os, sys

def render(out, fps):
    image_folder = '../images'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(out, 0, fps, (width,height))

    print("Rendering video..")

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

    print("Successfully renderer video!")