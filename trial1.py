from ultralytics import YOLO
import cv2
import os
import numpy as np
i = 0
model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.1

img0 =  np.zeros((1000,1000, 3), dtype=np.uint8)

cap = cv2.VideoCapture("D:/coding/cv projects/manohar/papaya_video2.mp4")  # Use default camera (change to 1, 2, etc., if you have multiple cameras)

while True:
    ret, frame = cap.read()
    cap.set(cv2.CAP_PROP_FPS,20) 
    if not ret:
        break

    H, W, _ = frame.shape
    key = cv2.waitKey(1) & 0xFF
    if key == 13:  # 13 is the ASCII code for Enter key
        # Capture the frame as an image
        i += 1
        cv2.imwrite(f'captured_image{i}.jpg', frame)
        print("Image captured successfully!")

    if i > 0:
        img = cv2.imread(f'captured_image{i}.jpg')

        results = model(img)[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            print("class id  = ",class_id)
            if score > threshold:
                print(f"Detected: {results.names[int(class_id)]} with confidence: {score}")
                # cv2.rectangle(img, (int(12), int(23)), (int(78), int(45)), (0, 255, 0), 4)
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
                # cv2.putText(img, results.names[int(class_id)].upper(), (int(x1), int(y1 - 30)),
                        #    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)   
                img0 = img[int(y1):int(y2), int(x1):int(x2)]
    if i > 0:
        
        img0 = cv2.resize(img0,(800,700))
        lower_bound = np.array([109,35,0])
        upper_bound = np.array([126,80,255])
        hsv_ima0 = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
        mask0 = cv2.inRange(hsv_ima0, lower_bound, upper_bound)
        mask10 = cv2.bitwise_not(mask0)


        roi0 = cv2.bitwise_and(img0, img0, mask = mask10)
        hsv_roi0= cv2.cvtColor(roi0, cv2.COLOR_BGR2HSV)

        average_color0 = cv2.mean(hsv_roi0)
        per= int((average_color0[1])/1.8)
        if per>100:
            per=100
        text = f" Ripeness Percentage = {per}% "
        cv2.rectangle(img0,(0,650),(800,695),(255,255,255),-1)
        cv2.putText(img0, text, (200, 680), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        print(" avegage color0 (HSV) = ", per)
        #cv2.line(img0,(0,650),(800,650),(255,255,255),10,1)
        cv2.imshow("img0",img0)

        cv2.imshow('Camera Feed', img)
    


    cv2.imshow("camera", frame)
    # # Exit the loop if the 'q' key is pressed
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
