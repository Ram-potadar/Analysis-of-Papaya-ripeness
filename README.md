# Papaya Ripeness Detection using YOLOv8 and OpenCV

This project uses a custom-trained YOLOv8 model and OpenCV to detect papayas in a video and calculate their ripeness percentage based on color analysis in HSV space.

## 🧠 Features

- Detects papayas using a YOLOv8 object detection model.
- Allows you to capture a frame manually by pressing the **Enter** key.
- Calculates the ripeness of the detected papaya using HSV color thresholds.
- Displays the ripeness percentage over the fruit.

## 🛠 Requirements

- Python 3.8+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- NumPy

### Install dependencies:

```bash
pip install ultralytics opencv-python numpy
```

### 📂 Project Structure

```bash
project/
│
├── trial_1.py
├── runs/
│   └── detect/
│       └── train/
│           └── weights/
│               └── best.pt   # Your trained YOLOv8 model
└── papaya_video2.mp4         # Input video file
```

### 🚀 How to Run
1. Place your custom-trained best.pt file in the path: ./runs/detect/train/weights/.
2. Ensure the input video path (papaya_video2.mp4) is valid.
3. Run the script:
```bash
python trial_1.py
```
4. While the video is playing:
     - Press Enter to capture a frame.
     - The YOLO model will detect the papaya, crop it, and analyze its ripeness.
     - Press Esc to exit.

### 🖼 Output
- Displays the current video frame.
- Shows the detected fruit region with a bounding box.
- Overlays the ripeness percentage.



