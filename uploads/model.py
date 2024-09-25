# from ultralytics import YOLO
#
# # Load the YOLOv8 model with your custom-trained weights
# model = YOLO('/Users/ananthakumaralwarsamy/PycharmProjects/pythonyolo8/yolov8.pt')
#
#
# def detect_fruit(image_file):
#     # Perform the prediction
#     results = model.predict(image_file)
#
#     # Assuming the results contain the classes and bounding boxes,
#     # you may want to format them for display.
#     fruit_info = []
#     for result in results:
#         for box in result.boxes:
#             fruit_info.append({
#                 'class': model.names[int(box.cls)],
#                 'confidence': float(box.conf),
#                 'bbox': box.xyxy.tolist()
#             })
#     return fruit_info
import os
from ultralytics import YOLO
from PIL import Image
import io


def convert_image_to_jpg(image_path):
    image = Image.open(image_path)
    if image.format not in ['JPEG', 'PNG', 'BMP']:
        image = image.convert('RGB')
        image.save(image_path, format='JPEG')

def detect_fruits(image_path):
        model = YOLO('C:/Users/HAI/PycharmProjects/pythonYoloProject/yolov8.pt')
        results = model(image_path)  # Perform detection

        # Debug print statements
        print("Detection Results:", results)

        # Extract detected class names (fruit names)
        fruit_names = [result.names[int(class_id)] for result in results for class_id in result.boxes.cls]

        # Debug print statements
        print("Detected Fruit Names:", fruit_names)

        # Return the detected fruit names and image path
        return fruit_names, image_path