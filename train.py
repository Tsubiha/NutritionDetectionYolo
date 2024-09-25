from ultralytics import YOLO

# Load a YOLOv8 model
model = YOLO('yolov8n.yaml')  # Use the YOLOv8 nano model for training

# Train the model
model.train(data='data.yaml', epochs=10, imgsz=300, batch=12, name='yolov8-fruits')

# Save the model weights
model.save('models/yolov8-fruits.pt')
