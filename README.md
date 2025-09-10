<pre>
BlueEye – Classroom Student Counter 🎓👁️

BlueEye is a computer vision project that uses YOLOv8 to detect and count students in a classroom video. It processes video frames, finds where the maximum number of students appear, and saves the best frame with bounding boxes.

📂 Repository Structure
.
├── app.py                   # Main script to run face detection
├── classroom.mp4            # Sample classroom video
├── debug_frame.jpg          # Debug image (example frame)
├── main_testing.mp4         # Test video 1
├── main_testing_2.mp4       # Test video 2
├── model.pt                 # Custom trained YOLO model (if any)
├── output.mp4               # Processed video output
├── output_classroom.jpg     # Best frame from classroom.mp4
├── output_main_testing.jpg  # Best frame from main_testing.mp4
├── output_main_testing_2.jpg# Best frame from main_testing_2.mp4
├── yolov8n-face.pt          # Pretrained YOLOv8 face detection model
├── yolov8n.pt               # General YOLOv8 model
└── README.md                # Project documentation

🛠️ Installation

Clone the repository:

git clone https://github.com/your-username/blueeye.git
cd blueeye


Install dependencies:

pip install ultralytics opencv-python


Place your input video in the project folder (or use the provided ones).

🚀 Usage

Run the main script:

python app.py


The script will:

Load the video (classroom.mp4, main_testing.mp4, or main_testing_2.mp4).

Detect faces frame by frame using YOLOv8.

Track the maximum number of detected students.

Save the best frame (with bounding boxes) as output_<video_name>.jpg.

Optionally, generate a processed video (output.mp4).

⚙️ Configuration

You can modify parameters inside app.py:

VIDEO = "classroom.mp4"   # Input video file
MODEL = "yolov8n-face.pt" # YOLOv8 face detection model
CONF = 0.35               # Confidence threshold
IMG_SIZE = 1280           # Image size for detection

🖼️ Example Outputs

Output Image: output_classroom.jpg → Best frame with faces highlighted.

Output Video: output.mp4 → Processed video with detections.

📖 Notes

Works best with clear, well-lit classroom videos.

You can swap yolov8n-face.pt with your own trained model (model.pt).

Larger YOLO models (yolov8s, yolov8m, etc.) may give better accuracy but will run slower.

🚀 Future Improvements

Real-time classroom monitoring via webcam.

Automated attendance tracking.

Integration with student databases.

✍️ Developed as part of the BlueEye Project – AI-powered classroom student counting.

  </pre>

