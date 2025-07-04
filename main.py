import cv2
import mediapipe
import virtual_mouse as vm


cam = cv2.VideoCapture(0)
mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7,
    max_num_hands = 1
)

try:
    while cam.isOpened():
        val, frame = cam.read()
        draw = mediapipe.solutions.drawing_utils

        if val:
            frame = cv2.flip(frame,1)
            frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            process = hands.process(frameRGB)

            landmarks_list = []
            if process.multi_hand_landmarks:
                hand_landmark_one = process.multi_hand_landmarks[0]
                draw.draw_landmarks(frame,hand_landmark_one,mpHands.HAND_CONNECTIONS)

                for lm in hand_landmark_one.landmark:
                    landmarks_list.append((lm.x,lm.y))
            
            vm.detect_gesture(landmarks_list,process)
        else:
            break      
            

        cv2.imshow("Mirror Frame",frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cam.release()
    cv2.destroyAllWindows()