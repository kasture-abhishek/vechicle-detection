# 🚗 Vehicle Detection and Counting Using OpenCV

This project demonstrates a **vehicle detection and counting system** developed using **Python and OpenCV**. The system processes a video file, detects moving vehicles using **background subtraction**, and counts them when they cross a predefined virtual line.

---

## 📌 Features
- Detects moving vehicles from video footage
- Counts vehicles crossing a reference line
- Uses Background Subtraction (MOG algorithm)
- Noise reduction using morphological operations
- Displays bounding boxes, center points, and live counter
- Real-time visual output

---

## 🛠️ Technologies Used
- Python
- OpenCV (opencv-contrib-python)
- NumPy

---

## ⚙️ How It Works
1. Video frames are read using OpenCV.
2. Frames are converted to grayscale and blurred.
3. Background subtraction (MOG) is applied to detect moving objects.
4. Morphological operations remove noise.
5. Contours are detected and filtered by size.
6. Vehicles are counted when they cross a predefined line.

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install opencv-contrib-python numpy
