import cv2
import os
from shutil import copyfile


def detect_faces(input_path, output_path,
                 open_cv_classifier="/home/rogia/Documents/git/opencv/OpenCV/data/haarcascades/haarcascade_frontalface_default.xml"):
    os.mkdir(os.path.join(output_path, "no-faces"))
    os.mkdir(os.path.join(output_path, "contains-faces"))
    face_cascade = cv2.CascadeClassifier(open_cv_classifier)
    images = os.listdir(input_path)
    print(images)
    for i, img in enumerate(images):
        src = os.path.join(input_path, img)
        imag = cv2.imread(src)
        gray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            dst = os.path.join(f"{output_path}/contains-faces", img)
        else:
            dst = os.path.join(f"{output_path}/no-faces", img)

        copyfile(src, dst)

if __name__ == '__main__':
    detect_faces(input_path="/home/rogia/Documents/AI4GOOD", output_path="/home/rogia/Documents/git/gender_bias/data")