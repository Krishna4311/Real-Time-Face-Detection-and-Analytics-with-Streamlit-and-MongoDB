# Real-Time Face Detection and Analytics Dashboard

This project is a real-time face detection and analytics system using OpenCV and MongoDB. Detected faces from webcam input are logged with timestamps into MongoDB, and insights are visualized using an interactive Streamlit dashboard.

---

## Features

- Real-time face detection using OpenCV's DNN module
- Frame deduplication and intelligent logging logic
- MongoDB integration for logging face detection events
- Streamlit dashboard with:
  - Face count per minute
  - Average faces per hour
  - Date vs. hour heatmap
  - CSV export and auto-refresh

---

## Model Used

The face detector is based on OpenCV’s SSD with ResNet-10 backbone trained on the WIDER FACE dataset.

- **Model Config (`deploy.prototxt`)**:  
  [Download from OpenCV GitHub](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt)

- **Model Weights (`res10_300x300_ssd_iter_140000_fp16.caffemodel`)**:  
  [Download from OpenCV GitHub](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel)

---
# Real-Time Face Detection and Logging System

A real-time face detection system using OpenCV’s deep learning-based face detector. It logs face counts to MongoDB and visualizes them through a Streamlit dashboard.

---

##  Setup Guide

Follow these steps to install, configure, and run the application.

---

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/face-detection-dashboard.git
cd face-detection-dashboard
```

---

### 2. Download Pre-trained Model Files

Download the model files and place them in the root directory of the project:

- [deploy.prototxt]
- [res10_300x300_ssd_iter_140000_fp16.caffemodel]

---

### 3. Install Python Dependencies

Make sure Python 3.7 or higher is installed.

```bash
pip install -r requirements.txt
```

---

### 4. MongoDB Setup

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create a free cluster.
3. Create a database named `face_log_db` and a collection named `detections`.
4. In `db.py`, replace the placeholder with your MongoDB connection URI:

If you prefer using environment variables, use the `python-dotenv` package.

---

### 5. Run the Face Detection Script

Start the face detection and logging service:

```bash
python detect.py
```

This opens your webcam, detects faces, and logs detection data (count + timestamp) to MongoDB every few seconds.

---

### 6. Run the Streamlit Dashboard

Launch the analytics dashboard in your browser:

```bash
streamlit run app.py
```

Features:
- Real-time graph of detected face counts per minute.
- Hourly average face count chart.
- Heatmap of detections (hour vs date).
- Raw data table and CSV export.

---

You can modify the cooldown time and confidence threshold in `detect.py` to fit your scenario (e.g., crowded environments, sensitive detection).

---

### Project Structure

```
.
├── dashboard.py         # Streamlit dashboard
├── main.py              # Real-time face detection and logging
├── db.py                # MongoDB connection logic
├── libs.py              # All imports
├── deploy.prototxt      # Face detection model architecture
├── res10_*.caffemodel   # Face detection weights
└── requirements.txt     # Python dependencies
```

---

### License for Model

The model used (`res10_300x300_ssd_iter_140000_fp16.caffemodel`) is distributed with OpenCV under the Apache License 2.0.

- Source: https://github.com/opencv/opencv
- License: https://www.apache.org/licenses/LICENSE-2.0

---





