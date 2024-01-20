from ultralytics import YOLO
import cv2
import math
from punto_centrale_persona import centro_rettangolo
from freccia import angolo_freccia, freccia_on_screen
from velocità import speed
from tracking_1_persona import  x_più_vicina
width = 1920
height = 1080
velocità = 0
x = []
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
# model
model = YOLO("yolo-Weights/yolov8n.pt")
model.conf = 0.70

# object classes
classNames = ["persona", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes
        n_persone = 0

        for box in boxes:
            cls = int(box.cls[0])
            # bounding box
            if classNames[cls] == "persona":
                n_persone = n_persone + 1
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                centro = centro_rettangolo(x1, y1, x2, y2)
                velocità = speed(x1, x2)
                x.append(centro[0] - (width / 2))

                cv2.circle(img, (int(centro[0]),int(centro[1])), 5, (0,0,255), 5)
                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
                # confidence
                confidence = math.ceil((box.conf[0]*100))/100
                print("Confidence --->",confidence)

                # class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])

                cv2.putText(img, classNames[cls], [x1, y1], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

    cv2.putText(img, str(velocità), (int(width / 100 * 75), int(height / 100 * 65)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 1)
    cv2.putText(img, str(n_persone), (int(width / 100 * 85), int(height / 100 * 70)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 1)
    if n_persone > 0:
        x_attendibile = x_più_vicina(x)
        print(x_attendibile)
        print(x)
        x.clear()
        angolo = angolo_freccia(x_attendibile, height, width)
        cord_su_screen = freccia_on_screen(x_attendibile, width, height)
        cv2.circle(img, (int(x_attendibile + (width / 2)), int(height / 2)), 7, (255,255,255), 7)
        cv2.arrowedLine(img, (int(cord_su_screen[1]), int(cord_su_screen[2])),(int(cord_su_screen[0]), int(cord_su_screen[3])), (0,0,255),2)
        cv2.putText(img, str(angolo), (int(width / 100 * 70), int(height / 100 * 95)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0), 1)



    cv2.imshow('Webcam', img)



    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()