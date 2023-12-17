import cv2
import os


def has_face(image_path):
    img = cv2.imread(image_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

    if len(face) > 0:
        return True
    else:
        return False


def delete_images_without_faces(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check for image files
            file_path = os.path.join(folder_path, filename)
            if not has_face(file_path):
                os.remove(file_path)
                print(f"Deleted: {filename}")

# Replace 'path_to_folder' with the path to your image folder
folder_path = 'C:/Users/User/Desktop/all_images_scaled2'
delete_images_without_faces(folder_path)
