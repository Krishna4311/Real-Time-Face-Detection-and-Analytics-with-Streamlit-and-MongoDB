from libs import * 
from db import collection  

# Load DNN face detection model
net = cv2.dnn.readNetFromCaffe('./deploy.prototxt', './res10_300x300_ssd_iter_140000_fp16.caffemodel')

# State variables
last_logged_time = 0
cooldown_seconds = 30
previous_face_count = -1  # to track change in face count

def detect_faces_dnn(frame):
    global last_logged_time, previous_face_count

    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    current_face_count = 0
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.3:
            current_face_count += 1
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"Face: {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    now = time.time()

    # Log to DB only if face count changed or cooldown passed
    should_log = False

    if current_face_count != previous_face_count:
        should_log = True
    elif current_face_count > 0 and (now - last_logged_time > cooldown_seconds):
        should_log = True

    if should_log:
        collection.insert_one({
            "timestamp": datetime.now().isoformat(),
            "face_count": current_face_count
        })
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Logged {current_face_count} face(s) to DB.")
        last_logged_time = now
        previous_face_count = current_face_count

    return frame

# --- Main Execution ---
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = detect_faces_dnn(frame)
    cv2.imshow('Face Detection (DNN)', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
