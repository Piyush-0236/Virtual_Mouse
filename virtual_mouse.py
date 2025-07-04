import pyautogui
from pynput.mouse import Button,Controller
import mediapipe
import time
import features as f
import util
import keyboard

screen_width , screen_height = pyautogui.size()
mouse = Controller()
mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7,
    max_num_hands = 2
)
def find_finger_tip(process):
    if process.multi_hand_landmarks:
        hand_landmark = process.multi_hand_landmarks[0]
        return hand_landmark.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]

def movemouse(index_finger_tip):
    if index_finger_tip is not None:
        x = int(index_finger_tip.x * screen_width)
        y = int(index_finger_tip.y * screen_height)
        pyautogui.moveTo(x,y)

def detect_gesture(landmarks_list,process):
    if len(landmarks_list) >= 21:
        index_finger_tip = find_finger_tip(process)
        thumb_finger_dist = util.get_distance((landmarks_list[4],landmarks_list[5]))

        if thumb_finger_dist < 20 and util.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) > 90:
            movemouse(index_finger_tip)
        
        elif f.is_left_click(thumb_finger_dist,landmarks_list):
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(0.5)

        elif f.is_right_click(thumb_finger_dist,landmarks_list):
            mouse.press(Button.right)
            mouse.release(Button.right)
            time.sleep(0.5)
        
        elif f.is_double_click(thumb_finger_dist,landmarks_list):
            pyautogui.doubleClick()
            time.sleep(0.5)

        elif f.is_minimize(thumb_finger_dist,landmarks_list):
            pyautogui.hotkey('alt','space')
            time.sleep(0.1)
            pyautogui.press('n')

        elif f.is_destroy(thumb_finger_dist,landmarks_list):
            pyautogui.hotkey('alt','space')
            time.sleep(0.1)
            pyautogui.press('c')
        
        elif f.all_windows(landmarks_list):
            keyboard.press("windows")
            keyboard.press("tab")
            keyboard.release("windows")
            keyboard.release("tab")
            time.sleep(0.4)

        elif f.sound_up(landmarks_list):
            pyautogui.press("volumeup")
            time.sleep(0.1)

        elif f.sound_down(landmarks_list):
            pyautogui.press("volumedown")
            time.sleep(0.1)