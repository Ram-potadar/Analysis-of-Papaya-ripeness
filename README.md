Papaya Ripeness Detection using YOLOv8 and OpenCV
This project uses a custom-trained YOLOv8 model and OpenCV to detect papayas in a video and calculate their ripeness percentage based on color analysis in HSV space.

🧠 Features
Detects papayas using a YOLOv8 object detection model.

Allows you to capture a frame manually by pressing the Enter key.

Calculates the ripeness of the detected papaya using HSV color thresholds.

Displays the ripeness percentage over the fruit.

🛠 Requirements
Python 3.8+

Ultralytics YOLOv8

OpenCV

NumPy

Install dependencies:
bash
Copy
Edit
pip install ultralytics opencv-python numpy
📂 Project Structure
bash
Copy
Edit
project/
│
├── your_script.py
├── runs/
│   └── detect/
│       └── train/
│           └── weights/
│               └── best.pt   # Your trained YOLOv8 model
└── papaya_video2.mp4         # Input video file
🚀 How to Run
Place your custom trained best.pt file in the path: ./runs/detect/train/weights/.

Ensure the input video path (papaya_video2.mp4) is valid.

Run the script:

bash
Copy
Edit
python your_script.py
While the video is playing:

Press Enter to capture a frame.

The YOLO model will detect the papaya, crop it, and analyze its ripeness.

Press Esc to exit.

🧪 How Ripeness is Calculated
Converts the cropped fruit region to HSV.

Applies a color mask to isolate ripe areas.

Calculates the average saturation to estimate ripeness percentage.

🖼 Output
Displays the current video frame.

Shows the detected fruit region with a bounding box.

Overlays the ripeness percentage.

🔒 Notes
Make sure the lighting in the video is consistent for accurate color-based analysis.

The HSV thresholds may need tuning based on the environment and fruit variety.

📧 Contact
For any questions or improvements, feel free to reach out.
