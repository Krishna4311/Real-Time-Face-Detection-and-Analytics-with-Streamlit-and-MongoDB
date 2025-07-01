# Real-Time Face Detection and Analytics Dashboard

This project is a real-time face detection and analytics system using OpenCV and MongoDB. Detected faces from webcam input are logged with timestamps into MongoDB, and insights are visualized using an interactive Streamlit dashboard.

---

## 📌 Features

- Real-time face detection using OpenCV's DNN module
- Frame deduplication and intelligent logging logic
- MongoDB integration for logging face detection events
- Streamlit dashboard with:
  - Face count per minute
  - Average faces per hour
  - Date vs. hour heatmap
  - CSV export and auto-refresh

---

## 🧠 Model Used

The face detector is based on OpenCV’s SSD with ResNet-10 backbone trained on the WIDER FACE dataset.

- **Model Config (`deploy.prototxt`)**:  
  [Download from OpenCV GitHub](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt)

- **Model Weights (`res10_300x300_ssd_iter_140000_fp16.caffemodel`)**:  
  [Download from OpenCV GitHub](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel)

---



