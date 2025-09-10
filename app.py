import os
import cv2
from ultralytics import YOLO

VIDEO = "main_testing_2.mp4"
MODEL = "yolov8n-face.pt"
CONF = 0.35       # confidence threshold
IMG_SIZE = 1280   # larger helps small faces

# Output filename based on video name
video_name = os.path.splitext(os.path.basename(VIDEO))[0]
OUTPUT_FILE = f"output_{video_name}.jpg"

# Load model
print("Loading model:", MODEL)
model = YOLO(MODEL)
print("Classes:", model.names)

cap = cv2.VideoCapture(VIDEO)
if not cap.isOpened():
    raise SystemExit(f"Couldn't open video: {VIDEO}")

max_faces = 0
best_frame = None
best_results = None

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1

    # Run YOLO inference
    results = model(frame, conf=CONF, imgsz=IMG_SIZE, verbose=False)[0]

    # Count faces (boxes)
    num_faces = len(results.boxes)

    if num_faces > max_faces:
        max_faces = num_faces
        best_frame = frame.copy()
        best_results = results

    # Optional: print progress every 50 frames
    if frame_count % 50 == 0:
        print(f"Processed {frame_count} frames... Max so far: {max_faces}")

cap.release()

if best_frame is not None:
    # Draw boxes on the best frame
    annotated = best_results.plot()

    # Save as output_<filename>.jpg
    cv2.imwrite(OUTPUT_FILE, annotated[:, :, ::-1])  # convert RGB->BGR
    print(f"✅ Saved {OUTPUT_FILE} with {max_faces} faces detected.")
else:
    print("⚠️ No frames processed.")
